from io import StringIO
import tokenize


source_code = """
 |-
"""

# 将字符串转换为类文件对象
stream = StringIO(source_code)

# 使用 tokenize.generate_tokens 生成标记
for token in tokenize.generate_tokens(stream.readline):
    print(f"{token.type} ({tokenize.tok_name[token.type]}): {token.string}")