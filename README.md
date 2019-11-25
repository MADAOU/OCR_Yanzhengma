# OCR_Yanzhengma
python、从创建验证码开始，到识别他。

详细内容可查看csdn博客： 
https://blog.csdn.net/weixin_43582101/article/details/91160276


上传的压缩包，里面有测试集和训练集，以及生成图片的.PY,分割的.PY，特征提取.PY和识别.PY。

最近喜欢先把测试结果图放前面。大家可以先看下效果。


![在这里插入图片描述](https://img-blog.csdnimg.cn/20190607214819920.gif)
识别速度并不是很快，代码并没有进一步优化。

本篇主要讲的是 从制作验证码开始，到我们利用机器学习识别出来结果的过程。

之前写过一篇利用opencv进行验证码处理，感兴趣可以看看，本篇的验证码并没有过多处理：https://blog.csdn.net/weixin_43582101/article/details/90609399


利用机器学习识别验证码的思路是：让计算机经过大量数据和相应标签的训练，计算机习得了各种不同标签之间的差别与关系。形成一个庞大的分类器。此时再向这个分类器输入一张图片。分类器将输出这个图片的“标签”。图片识别过程就完毕了。


下面我们正式开始本篇内容。


## 一：生成验证码
这里生成验证码的方式是使用了python的PIL库。 他已经是Python平台上的图像处理标准库了。PIL功能非常强大，API也非常简单易用。
还是去看csdn博客吧
