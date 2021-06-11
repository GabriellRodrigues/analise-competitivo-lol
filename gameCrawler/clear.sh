#!/bin/bash -xe
if [ $1 == "19" ];
then
        cd /home/$USER/.IntelliJIdea201*/config || true
        rm eval/idea*.evaluation.key || true
        sed -i '/evlsprt/d' options/other.xml || true
        cd ~/.java/.userPrefs/jetbrains || true
        rm -rf idea* || true
fi
if [ $1 == "20" ];
then
        rm -rf ~/.config/JetBrains/IntelliJIdea2021*/eval
        rm -rf ~/.config/JetBrains/IntelliJIdea2020*/eval
        sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/IntelliJIdea2021*/options/other.xml
        sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/IntelliJIdea2020*/options/other.xml
        rm -rf ~/.java/.userPrefs/jetbrains/idea
fi
if [ $1 == "py" ];
then
        rm -rf ~/.config/JetBrains/PyCharm2020*/eval
        rm -rf ~/.config/JetBrains/PyCharm2021*/eval
        sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/PyCharm2020*/options/other.xml
        sed -i -E 's/<property name=\"evl.*\".*\/>//' ~/.config/JetBrains/PyCharm2021*/options/other.xml
        rm -rf ~/.java/.userPrefs/jetbrains/idea
fi
