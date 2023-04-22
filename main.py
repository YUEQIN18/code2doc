from util import str_blocks, get_all_code
from chat import get_result
import os


# 生成每个代码块的接口文档，拼接后输出
# 所有代码块接口文档
def get_document_msgs(code_block_array):
    document_msgs = ''
    for code_block in code_block_array:
        print('正在生成接口文档...')
        text = '下面是项目的部分代码，请你分析它的结构，按照url地址、代码功能说明、传入参数说明、返回值参数说明生成一份markdown格式的项目接口文档\n' + code_block
        result = get_result(text)
        document_msgs += result + '\n'
    open('out/接口文档.md', 'w', encoding='utf-8').write(document_msgs)
    return document_msgs


# 生成总结
def get_all_document_msg(document_msgs):
    print('正在生成总结...')
    main_msg = get_result(
        '下面是对同一个项目的不同方法的描述，请把这些文档组合成一个文档\n'
        + document_msgs
    )
    main_msg = main_msg.replace('\n', '')
    open('out/总结.md', 'w', encoding='utf-8').write(main_msg)
    return main_msg


def get_all_content(main_msg: str):
    all_content = ''
    tasks_str = open('tasks', 'r', encoding='utf-8').read()
    tasks = tasks_str.splitlines()
    i = 1
    for task in tasks:
        print('正在生成正文：' + task)
        cmd = f'''
这是项目的介绍：{main_msg}
这是我要求的大纲：{'、'.join(tasks_str.splitlines())}
我不需要你编写大纲中所有内容，你只需要编写其中的一个模块“{task}”，而且不要超过 500 字。
            '''
        content = get_result(cmd)
        file_path = 'out/' + str(i) + '. ' + task
        i += 1
        open(file_path, 'w', encoding='utf-8').write(content)
        all_content += content + '\n'
    open('out/完整文档.md', 'w', encoding='utf-8').write(all_content)
    return all_content


if not os.path.exists('out'):
    os.mkdir('out')

if __name__ == '__main__':
    input_code: str = get_all_code('code')
    print('源代码整理完成，共 ' + str(len(input_code.splitlines())) + ' 行')
    code_block_array = str_blocks(input_code)  # 代码块列表
    document_msgs = get_document_msgs(code_block_array)  # 所有文档
    # main_msg = get_main_msg(document_msgs)  # 总结
    # all_content = get_all_content(main_msg)  # 完整文章内容
    print('完成')
