import random

energy_advice = []
energy1 = "食事の量を減らして回数を増やしたり、水分を多くとるようにしましょう！\n"
energy2 = " 繊維質が多い野菜や、タンパク質は食欲を抑えてくれる効果があります。\n"
energy3 = "油類は、同じ量でも炭水化物やタンパク質の2倍以上カロリーがあるので \
                摂取カロリーを抑えるために注意しましょう！\n"
energy_advice.append(energy1)
energy_advice.append(energy2)
energy_advice.append(energy3)

protein_advice = []
protein1 = "タンパク質は動かなくても、食べた3割のエネルギーが代謝によって消費されるので、\
            意識的に高タンパクな食事を意識してみましょう。\n"
protein2 = "タンパク質を取れる食材として、イカや海老・貝類なども脂質が少なくダイエットに向いているので \
            鶏むね肉やささみに飽きたらおススメです。\n"
protein3 = "なかなかタンパク質を多くとるのが大変な方には、プロテインを取り入れてみるのもいいでしょう。 \
            食事の前に飲むと食欲を抑えることもできます！\n"
protein_advice.append(protein1)
protein_advice.append(protein2)
protein_advice.append(protein3)

fat_advice = []
fat1 = "油を少なくする方法として、「茹でる・蒸す・焼く」という調理方法に変えてみましょう！ \
        揚げ物はとらないくらいの意識だとうまくいくはずです。 また、揚げ物やドレッシングに注意しましょう。\n"
fat2 = "赤身肉や貝類は脂が少なく、良質なタンパク質が摂取できるので、積極的に選びましょう。\
        脂の乗った魚やお肉はおいしいですが注意が必要です！\n"
fat3 = "余裕があれば、脂質の摂取量を減らすのと同時に、普段使っている油をオリーブオイルやごま油に変えたり \
        アボカドやナッツから取ってみましょう。\n"
fat_advice.append(fat1)
fat_advice.append(fat2)
fat_advice.append(fat3)

carbo_advice = []
carbo1 = "炭水化物の量を減らすために、普段お米を取っているなら玄米に変えてみましょう。 \
        オートミールやさつまいもなどもお腹にもたまりやすいのでお米の置き換えにおススメです。\n"
carbo2 = "お腹が空いているときに食べるとついつい、食べ過ぎてしまうため間食を取り入れて、 \
        ドカ食い防止を意識しましょう！\n"
carbo_advice.append(carbo1)
carbo_advice.append(carbo2)

def make_advice(reduce_info, energy, protein, fat, carbo, text):
    if  reduce_info["reduce_cal"] < energy:
        text += "全体的な摂取カロリーが多いようです。"
        text += random.choice(energy_advice)
    if protein*4 < energy*0.25:
        text += "タンパク質の摂取量が少なめのようです。"
        text += random.choice(protein_advice)
    if energy*0.2 < fat*9:
        text += "脂質の摂取量を控えましょう。"
        text += random.choice(fat_advice)
    if energy * 0.55 < carbo*4:
        text += "炭水化物の摂取量に注意してください。"
        text += random.choice(carbo_advice)
    if not text:
        text += "栄養バランスも完璧で、カロリーも目標値以内となっています！うまく食事管理ができているようです。\n \
                その調子で目標まで進んでいきましょう！"
    
    return text
