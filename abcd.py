{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Charlie0603/123.py/blob/main/abcd.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "import re\n",
        "\n",
        "from requests.api import patch\n",
        "url1 = 'https://invoice.etax.nat.gov.tw/'\n",
        "html1 = requests.get(url1)\n",
        "sp = BeautifulSoup(html1.text, 'lxml')\n",
        "all1 = sp.find(\"table\", class_=\"etw-table-bgbox etw-tbig\")\n",
        "#print(all1)\n",
        "\n",
        "tb = sp.find('span', class_='font-weight-bold etw-color-red')\n",
        "st.write(\"特別獎:\", tb.text)\n",
        "#可用replace替代調文本內文字\n",
        "t = sp.find_all('span', class_='font-weight-bold etw-color-red')[1]\n",
        "st.write(\"特獎:\", t.text)\n",
        "\n",
        "head1 = sp.find(\"p\", class_=\"etw-tbiggest mb-md-4\")\n",
        "head2 = sp.find_all(\"p\", class_=\"etw-tbiggest mb-md-4\")[1]\n",
        "head3 = sp.find_all(\"p\", class_=\"etw-tbiggest mb-md-4\")[2]\n",
        "st.write(\"頭獎:\", head1.text, end=\"\")\n",
        "st.write(head2.text, end=\"\")\n",
        "st.write(head3.text)\n",
        "\n",
        "add1 = sp.find_all(\"span\", class_=\"font-weight-bold etw-color-red\")\n",
        "st.write(\"增開六獎:\", add1[-1].text)\n",
        "\"\"\"\n",
        "td = \"14872301\"\n",
        "tb = \"37250799\"\n",
        "t = [\"71086085\", \"53645821\", \"46626911\"]\n",
        "No6 = \"916\"\n",
        "\"\"\"\n",
        "a = str(input(\"請輸入你的發票號碼:\"))\n",
        "a_3 = a[-3] + a[-2] + a[-1]\n",
        "headlist = [head1.text.replace(\"\\n\", \"\"), head2.text.replace(\"\\n\", \"\"), head3.text.replace(\"\\n\", \"\")]\n",
        "while a != \"\":\n",
        "    b = 0                       #對發票末數\n",
        "    b_con = 0                   #發票連續對中號碼\n",
        "    b_con1 = 0                  #連續對中的最大數\n",
        "    a_3 = a[-3] + a[-2] + a[-1] #再次更新後三碼\n",
        "    for i in headlist:\n",
        "        #print(i)\n",
        "        b = 0\n",
        "        for j, k in zip(reversed(i), reversed(a)):\n",
        "            if j == k:\n",
        "                b = b + 1\n",
        "                #print(j, k, b)\n",
        "            else:\n",
        "                b_con = b\n",
        "                if b_con > b_con1:\n",
        "                    b_con1 = b_con\n",
        "                break\n",
        "\n",
        "    #print(\"最高連續:\", b_con1)\n",
        "    headlistF = False      #判斷頭獎\n",
        "\n",
        "    if len(a) == 8:\n",
        "        for l in headlist:\n",
        "            if l == a:\n",
        "                print(\"恭喜中獎二十萬，走吧!吃點好料的!\")\n",
        "                headlistF = True\n",
        "        if tb.text == a:\n",
        "            st.write(\"恭喜中獎一千萬，恭喜乾爹!\")\n",
        "        elif t.text == a:\n",
        "            st.write(\"恭喜中獎兩百萬，缺乾兒子嗎?\")\n",
        "        elif b_con1 == 7 :\n",
        "           st.write(\"恭喜中獎4萬元~\")\n",
        "        elif b_con1 == 6:\n",
        "            st.write(\"恭喜中獎一萬元~\")\n",
        "        elif b_con1 == 5:\n",
        "            st.write(\"恭喜中獎四千元~\")\n",
        "        elif b_con1 == 4:\n",
        "            st.write(\"恭喜中獎一千元~\")\n",
        "        elif b_con1 == 3 or a_3 == add1[-1].text:\n",
        "            st.write(\"恭喜中獎兩百元~\")\n",
        "        elif headlistF == False:\n",
        "            st.write(\"殘念~本次貢龜~\")\n",
        "    else:\n",
        "        st.write(\"請輸入八位數的發票號碼!\")\n",
        "    a = str(input(\"再次輸入你的發票號碼(輸入空值為結束):\"))\n",
        "    st.write('謝謝使用，祝您中獎')\n",
        "    break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 375
        },
        "id": "qFNy-LBuWVpY",
        "outputId": "11a2fbe9-d110-4add-b515-35edc1167fdb"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-811424879737>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mbs4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mre\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mrequests\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapi\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpatch\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    }
  ]
}