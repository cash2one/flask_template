# -*- coding: utf-8 -*-
from flask_script import Command

from module.scraping.inspection import InspectionWord

# from
# http://dic.nicovideo.jp/a/%E3%83%8B%E3%82%B3%E3%83%8B%E3%82%B3%E7%94%9F%E6%94%BE%E9%80%81%3A%E9%81%8B%E5%96%B6ng%E3%83%AF%E3%83%BC%E3%83%89%E4%B8%80%E8%A6%A7
INSPECTION_WORD = [
    "陰毛",
    "いんもう",
    "まんこ",
    "ま○こ",
    "まんk",
    "マソコ",
    "オメコ",
    "ヴァギナ",
    "クリトリス",
    "ちんこ",
    "ちんk",
    "あほか",
    "ちんちん",
    "チンポ",
    "チン毛",
    "ちん毛",
    "ペニス",
    "penis",
    "きんたま",
    "肉棒",
    "勃起",
    "尻",
    "ボッキ",
    "精子",
    "精液",
    "精えき",
    "射精",
    "顔射",
    "ザーメン",
    "●～",
    "○～",
    "セックス",
    "セックル",
    "交尾",
    "SEX",
    "S○X",
    "体位",
    "淫乱",
    "アナル",
    "anus",
    "おっぱい",
    "oppai",
    "おっぱお",
    "巨乳",
    "きょにゅう",
    "きょにゅー",
    "貧乳",
    "ひんにゅう",
    "ひんにゅー",
    "谷間",
    "たにま",
    "何カップ",
    "なにカップ",
    "手ブラ",
    "てブラ",
    "パンツ",
    "パンティ",
    "パンt",
    "ノーパン",
    "乳首",
    "ちくび",
    "自慰",
    "オナニ",
    "オナ二",
    "オナヌ",
    "マスターベーション",
    "しこって",
    "しこしこ",
    "脱げ",
    "ぬげ",
    "脱いで",
    "ぬいで",
    "脱ごう",
    "ぬごう",
    "喘いで",
    "あえいで",
    "広告",
    "クンニ",
    "フェラ",
    "まんぐり",
    "パイズリ",
    "風俗",
    "ふうぞく",
    "ふーぞく",
    "ソープ",
    "デリヘル",
    "ヘルス",
    "姦",
    "包茎",
    "ほうけい",
    "童貞",
    "どうてい",
    "どうてー",
    "どーてー",
    "どーてい",
    "性器",
    "処女",
    "やりまん",
    "乱交",
    "バイブ",
    "ローター",
    "パイパン",
    "中出し",
    "中田氏",
    "スカトロ",
    "糞",
    "うんこ",
    "パコパコ",
    "ホモ",
    "homo",
    "ぱいぱい",
    "ノーブラ",
    "手コキ",
    "手マン",
    "潮吹",
    "罵倒・差別表現",
    "きめえ",
    "変態",
    "馬鹿",
    "ばーか",
    "baka",
    "fuck",
    "f*ck",
    "ファック",
    "不細工",
    "ぶさいく",
    "ブス",
    "かす",
    "基地外",
    "気違い",
    "ブタ",
    "くたばれ",
    "潰せ",
    "bitch",
    "転載",
    "ビッチ",
    "死す",
    "死な",
    "死ぬ",
    "しぬ",
    "死ね",
    "しね",
    "氏ね",
    "shine",
    "死の",
    "死ん",
    "ﾀﾋ",
    "死",
    "殺さ",
    "殺し",
    "殺す",
    "ころす",
    "殺せ",
    "ころせ",
    "殺そ",
    "乞食",
    "ばばあ",
    "ばばぁ",
    "BBA",
    "くず",
    "犯罪・非常識",
    "麻薬",
    "レイプ",
    "犯し",
    "創価",
    "■■■■■",
    "☆☆☆☆",
    "★★★★",
    "整形",
    "からきますた",
    "ௌ",
    "e三",
    ";ii",
    "　　　",
    "ヤク中",
    "通り魔",
    "[I|i][D|d]\:",
]


class InsertInspection(Command):
    """
    インスペクション辞書を登録する
    ベキ等性あり、連打可能
    """
    def run(self):
        InspectionWord.register(INSPECTION_WORD)
