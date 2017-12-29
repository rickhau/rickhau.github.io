---
title: Octopress on Windows
date: 2015-04-26 17:18:10 +0800
category: blog
comments: True
slug: octopress-windows
---
## Environment
Windows 7

### Pre-requisite ###
- This article is to setup my Windows 7 environment to write blog posts    
- Use octopress environment pushed by MacOS
- You have python 2.7 installed on your Windows 7
- Remaining taks on Windows 7:
  * Install RubyInstaller    
  * Clone git repository :octocat:    
  * Configure and continue the post    


### Configure environment ###

#### STEP 1: Install RubyInstaller

- Download and install rubyinstaller.exe  

<sp>[rubyinstaller](http://rubyinstaller.org/downloads/)</sp>

<sp>I picked up ruby-2.1.4(x64) to install</sp>  

<sp>
  [2.1.4(x64)](http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.1.4-x64.exe)   
</sp>
  
#### STEP 2: Install Ruby Development Kit

- Download and install `DevKit-mingw64-64-4.7.2-20130224-1432-sfx`

  I installed Ruby 2.1.4(x64), so the development kit I have to use is:    
  
  [For use with Ruby 2.0 and 2.1 (x64 - 64bits only)](http://dl.bintray.com/oneclick/rubyinstaller/DevKit-mingw64-64-4.7.2-20130224-1432-sfx.exe)
  
  I extract to `C:\Ruby21-Devkit` where my ruby was installed under `C:\Ruby21-x64`

  
    
#### STEP 3: Create ruby config.yml

- Open your windows terminal 

```
   > cd C:\Ruby21-Devkit    
   > ruby dk.rb init
   # This will generate a config.yml
```  

- Edit config.yml to add where you install the ruby

```
    ---
    - C:/Ruby21-x64
```

- Install it

```
    > ruby dk.rb install
```
  
####STEP 4: Update gem

- Run the following command:

```
    > gem update --system
```

  Then, you will see the following messages:

  
```
    SSL_connect returned=1 errno=0 state=SSLv3 read server certificate B: certificate verify failed
```

- Solve the SSL issue    

```
    # To get what gem version you have installed
   > gem --version
```

  1) Download RubyGems based on the gem version you have installed. 


   Picked up 2.2.x due to my system reports 2.2.2    
   * [2.2.x](https://github.com/rubygems/rubygems/releases/tag/v2.2.3)    
  
   Others:    
   * [1.8.x](https://github.com/rubygems/rubygems/releases/tag/v1.8.30)   
   * [2.0.x](https://github.com/rubygems/rubygems/releases/tag/v2.0.15)

  
  2) Run the following commands:
  
```
    C:\>gem install --local C:\rubygems-update-1.8.30.gem
    C:\>update_rubygems --no-ri --no-rdoc
    C:\>gem uninstall rubygems-update -x
```

  Congratulations! 
  
  3) Now, let's update gem  

```
     gem update --system
```
  Reference link:
  >- [SSL issue](https://gist.github.com/luislavena/f064211759ee0f806c88)

####STEP 5: Clone your git repository

- Please git clone your "source" branch not "master" branch    
  You can configure your github page using "source" as the default branch

```
    > git clone https://github.com/rickhau/rickhau.github.io.git
    > cd rickhau.github.io
    > gem install bundler
    > bundle install
```

- Preview your existing posts

```
    > rake preview
```

  Go to http://localhost:4000 to browse your old posts

####STEP 6: Write your new post

```
    > rake new_post["Your new post title"]
```

  Go to `source\_posts\` directory to edit your new markdown file for new article.
  

####STEP 7: Configure the UTF-8 encoding

```
    set LC_ALL=zh_TW.UTF-8
    set LANG=zh_TW.UTF-8
```

- Or you can write it in the .bat script to help you set the encoding automatically

```
    @echo off
    set LC_ALL=zh_TW.UTF-8
    set LANG=zh_TW.UTF-8
    rake generate
    rake preview
```

#### HAPPY WRITING!!!! #####
