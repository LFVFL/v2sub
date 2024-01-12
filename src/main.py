# 导入requests库，用于发送HTTP请求
import requests


# 定义一个函数，用于从给定的url中提取前缀为"https://oss.v2rayse.com/proxies/data/"的链接
def extract_links(url):
    # 发送GET请求，获取url的响应内容
    response = requests.get(url)
    # 如果响应状态码为200，表示请求成功
    if response.status_code == 200:
        # 获取响应内容的文本
        text = response.text
        # 定义一个空列表，用于存储提取的链接
        links = []
        # 定义一个常量，表示链接的前缀
        PREFIX = "https://oss.v2rayse.com/proxies/data/"
        # 遍历文本中的每一行
        for line in text.splitlines():
            # 如果行以链接的前缀开头，表示找到了一个链接
            if line.startswith(PREFIX):
                # 将链接添加到列表中
                links.append(line)
        # 返回提取的链接列表
        return links
    # 否则，表示请求失败，抛出异常
    else:
        raise Exception(f"请求失败，状态码为{response.status_code}")


# 定义一个函数，用于从给定的链接列表中获取每个链接的网页内容，并将它们合并到一个文件中
def merge_contents(links, filename):
    # 定义一个空字符串，用于存储合并的内容
    contents = ""
    # 遍历链接列表中的每个链接
    for link in links:
        # 发送GET请求，获取链接的响应内容
        response = requests.get(link)
        # 如果响应状态码为200，表示请求成功
        if response.status_code == 200:
            # 获取响应内容的文本
            text = response.text
            # 将文本添加到合并的内容中，用换行符分隔
            contents += text + "\n"
        # 否则，表示请求失败，抛出异常
        else:
            raise Exception(f"请求失败，状态码为{response.status_code}")
    # 打开一个文件，用写入模式
    with open(filename, "w", encoding="utf-8") as f:
        # 将合并的内容写入到文件中
        f.write(contents)


# 定义一个主函数，用于执行程序的逻辑
def main():
    # 定义一个常量，表示要提取链接的url
    URL = "https://shz.al/PSXr"
    # 定义一个常量，表示要合并内容的文件名
    FILENAME = "v2rayse_sub.txt"
    # 调用extract_links函数，从url中提取链接
    links = extract_links(URL)
    #  print(links)
    # 调用merge_contents函数，从链接中获取内容，并合并到文件中
    merge_contents(links, FILENAME)
    # 打印一个提示信息，表示程序执行成功
    print(f"程序执行成功，内容已合并到{FILENAME}文件中")


# 如果这个文件是作为主程序运行，调用main函数
if __name__ == "__main__":
    main()
