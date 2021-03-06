#!/usr/bin/python
#coding:utf-8
import sys
import os


# GENIA taggerの出力
# word1   base1   POStag1 chunktag1 NEtag1(固有表現タグ)

#ディレクトリ内のファイルリストを返す
def get_files(dirpath):
    flist = []
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(os.path.join(path)):
                flist.append(path)
    return flist


# taggingされたファイル群のディレクトリ
def get_docs_list(dirpath):
    docs = []
    for file_name in get_files(dirpath):
        sent = []
        text = []
        prev_tok = None
        for line in open(file_name):
            if line == "\n":
                text.append(sent)
                sent = []
                continue
            line_split = line.strip().split()
            tok = {"w": line_split[0], "lem": line_split[1],
                   "pos": line_split[2], "chunk": line_split[3],
                   "prev": prev_tok, "next": None}
            if prev_tok is not None:
                prev_tok["next"] = tok
            prev_tok = tok
            sent.append(tok)
        docs.append(text)
    return docs
