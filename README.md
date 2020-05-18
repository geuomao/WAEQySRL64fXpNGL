# MJJ扫域名脚本
## 功能
- 自动分离域名, 并判断
- 自动验证域名可以用作干什么
- 自动保存已扫描到的域名
- 接入Tor用于反爬虫
- 忘了
## 不足
- 不会自动停止
- 快过期域名不会保存(可以加, 等更新)
- 可能会抽风
- 凑数
- 强迫症
## 教程
~~下载脚本~~  
如果不会下载请点击这个链接:  
[怎么从Github下载文件](https://bdfy.azurewebsites.net/?%E6%80%8E%E4%B9%88%E4%BB%8EGithub%E4%B8%8B%E8%BD%BD%E6%96%87%E4%BB%B6)

~~借用某位大牛的一句话:~~  
> ~~下载了直接run 啊, python xxx.py就完事了, 缘分到了就不会报错~~

首先是你灵巧的双手  
然后是环境:  
```
pip install stem pySocket requests beautifulsoup4
```
~~requirements.txt~~  
~~requirements 这辈子都没有的~~  

~~环境都好了那么就是run了呗~~

最后, 是重中之重:  
- 第一步打开[Google Maps](https://www.google.com/maps)
- 第二步 搜索 Schools
  - 不懂的人可以看图
  ![1.png](https://i.loli.net/2020/05/18/g7rMSN3WDP8a2jw.png)
  ~~我没被旦总发往非洲, 真的没有, (旦总如果看到记得把我接回去)~~
- 第三步 选一个你喜欢的位置
  - 不懂的人继续看图
  ![2.png](https://i.loli.net/2020/05/18/KSNb3kwQxtlp2Ch.png)
  - 如果你是个小机灵鬼, 想必你也看到了, 没错, 上面有个**在此区域搜索** ~~点一下~~  
  点完了你就可以关掉浏览器去喝茶了, 因为你完全做错了
- 第四步 伸出你们天天撸东西的手, 用你的右手食指点击一下你键盘上的F12, 如果没有, 去把别人键盘上的F12扣下来按在你的键盘上
  - 不懂的人继续看图  
  ~~不会录像点击键盘的我没那么无聊~~  
  ![3.png](https://i.loli.net/2020/05/18/nHDFYRh2CkyxVcl.png)
  新的MJJ就要问了, 这是什么呀.  
  老的MJJ要告诉你, 这是资本主义留给我们撸资本主义羊毛的神兵利器  
- 第五步 继续用你们灵巧的右手的食指点击一下右边的 Network  
  ~~如果没有反应那么就把显示屏戳破~~  
  - 继续看图
  ![4.png](https://i.loli.net/2020/05/18/YuV4BQGIKZf6EJc.png)
- 第六步 点击那个第三步的 在此区域搜索
  - 还要看图? 没了
- 第七步 ~~咋还没完~~ 看图, 在框出来的地方输入 search
 -![5.png](https://i.loli.net/2020/05/18/xOVHkJgNnbFsA6h.png)
- 第八步 右键复制
  ```
  Copy -> Copy link address
  ```
- 第九步 复制到脚本的
   ```
    def google_map_get():
    下面的
    url 的 '' 里面
    ```
- 第十步 
  ```
    找到第一个 8i0
    把 0 改成 ' + str(count * 20) + '
  ```

行了现在可以跑了

```
python sym.py
```

坐等就好了

A1 域名会保存在目录下的 domain_A1.txt 里  
A1P 域名会保存在目录下的 domain_A1P.txt 里

没什么想说的了, 想到了再补充