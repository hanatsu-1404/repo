mg = "hello" #変数定義
print(mg)    #文字列出力
x = 2 * 3       # 数値計算 他の言語と同じ
xy = x + 6
print(mg +"%d" %(xy))   #数値を print するときは文字列フォーマットが必要
print("format test{0}".format(xy))  # format ってやつも使える
print("------------------\n")   # 改行は \n でできる      タブは \t でできる    
print((mg+"\n")*3)           # * で文字を複数回表示できる     ()で囲める。ブロックとして扱えて便利