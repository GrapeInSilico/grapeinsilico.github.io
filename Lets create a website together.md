# Let's create a website together

## 1st step : pre-requisites

In this tutorial, we will be creating a website using mainly one tool : 

- **Hugo** (goHugo)

![**Hugo** (goHugo)](/images_tuto/gohugo.io.png "goHugo")

It is a static web site generator which was coded in the [Go language](https://en.wikipedia.org/wiki/Go_(programming_language)).

### The go language

This open-source promgramming language can be download [here](https://go.dev/dl/).

![Download goHugo](/images_tuto/g0.gif)

### The goHugo tool

#### - Download goHugo

This open-source tool can be download (we highly recommand the extended version) [here](https://github.com/gohugoio/hugo/releases).

![Download goHugo](/images_tuto/g1.gif)
However, please note that it is not the only way to download the tool.

Check-out their installation guide [here](https://gohugo.io/getting-started/installing/).

#### - Add it to your PATH

If you downloaded it using the first link, you may want to extract the folder and add it to your PATH variable (in your environnement variables).

![goHugo folder](/images_tuto/goHugo_file.png)

Just type environnement variables in your start menu and you will see a new entry : **Path**.

![Environnement variables](/images_tuto/path.png)

![add Hugo to your path variable](/images_tuto/path2.png)

#### - (Optionnal but neithertheless recommanded) Use an code editor

In this tutorial, we will be using the [code editor](https://en.wikipedia.org/wiki/Source-code_editor) [**VSCode**](https://code.visualstudio.com/).

But you may choose to use any other code editor. In this tutorial, we are likely to manipulate a lot of files, so make sure the editor you choose helps you see threw file trees.

### Git

Make sure [git](https://git-scm.com/downloads) is installed

## 2nd step : create your first website

1. Open your shell / Command Prompt

2. Make sure goHugo had been correctely added to your PATH variable by typping the command :

```
hugo version
```

![hugo version command](/images_tuto/cmd1.png)

3. Go to the folder where you want to create your website :

    - Create a new folder if you don't have one yet.
    
    ```
    mkdir C:\Users\YourUserName\Documents\goHugo
    ```

    - If you are using `Windows`, you can use the command :
    
    ```
    cd C:\Users\YourUserName\Documents\goHugo
    ```
    
    - If you are using `MacOS`, you can use the command :
    
    ```
    cd ~/Documents/goHugo
    ```
    
    - If you are using `Linux`, you can use the command :
    
    ```
    cd ~/Documents/goHugo
    ```

4. Initialize your goHugo project :

    - Create a new project by typing the command :

    ```
    hugo new site 'The name of your website'
    ```
    In our demo we will be calling it 'MySuprWebSite'

    ![hugo new site _](/images_tuto/cmd2.png)

    This command will create a new folder called (in our case) 'MySuprWebSite' in the folder you specified.

    Plus, it will create a serie a folder and a new file called 'config.toml' in the folder 'MySuprWebSite'.

    ![new tree of folders](/images_tuto/supr_website.png)

5. Choose a theme for your website

    A goHugo website works with a [theme](https://themes.gohugo.io/).

    The idea consists in having a collection of premade templates and static files and using them as a base upon which we will create our website.

    Go to the https://themes.gohugo.io/ page and search for a theme you would like to use in your website.

    In our demo we will be calling it 'stack'
    ![theme Massive](/images_tuto/stack.png)

    Please note that some help concerning the theme that we will use is available below the image (althgough it is not always the case).

    If you click on this download button, you will be redirected to the github repository of the theme.
    You may want to copy its URL.
    ![Massive github repo](/images_tuto/stack_git.png)

6. Import this theme to your website file

    - First go to the folder 'The name of your website' in your shell

    - Then type the command :
    
    ```
    git init
    git submodule add <<gitHub adress of the theme you will use to create the website>> themes/<<name of the new folder name>>
    ```

    For instead : ![git submodule add](/images_tuto/cmd3.png)

    Create a new folder called 'stack' in your 'theme' folder and copy the theme gitHub repository into it.

    ![new folder into theme](/images_tuto/exp2.png)

## 3rd step : Customize your website

Go to the folder 'The name of your website' in your shell
    
Then type the command :
    
```
hugo server -D
```

This command will start a server on your computer, it takes the folder of your website into account and, when any changes are made, it will automatically refresh the website. 

Basically it allows you to see a preview of your website in your browser (here on http://localhost:1313/).

![Preview of your website](/images_tuto/cmd4.png)

(-D means that it will include drafts - this argument is optional)

For now the preview consists in a blank page, but it will be improved in the future.

![blank page](/images_tuto/Blank_page.png)

### Add the theme to your configuration file

While keeping your command active in your command prompt, you can add the theme to your configuration file.

Go to your 'The name of your website' folder, this time with your code editor and open the configuration file : `config.[toml, yaml or json]`.

Please add the line :

```
theme = 'the name of the folder in your <<theme>> folder'
```

![adding_theme](/images_tuto/vs1.png)

If you save the file and then refresh the preview website, it will use the theme you have just added.

![page_1](/images_tuto/p1.png)

By modifying the title line, you can change the title of your website.

![page_2](/images_tuto/p2.png)


**By modifying any line in your configuration file, you can modify your website. To see how to fulfill your needs, please check the theme help page.**

A good idea could be to copy the theme configuration file which is into your theme folder (**exampleSite**), paste it in the place of the initial configuration website and modify the theme line (to adapt the name) and other minus stuff.

![config](/images_tuto/vs2.png)

*Note* : if any error occurs or if you don't see any change, please reload the preview website in the command prompt : `Ctrl + C` & `hugo server -D`.

![summary](/images_tuto/demo1.gif)
