#!/usr/bin/env python3
"""Adds the build 3 help sections (marking your own answer, gas conditions) to copy.json.
Running it twice changes nothing. Run build_pages.py afterwards."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent / "copy.json"
D = json.loads(P.read_text())

# language: (updated line, (mark title, mark text), (gas title, gas text))
T = {
 "en-US": ("Last updated 14 November 2026",
  ("Marking your own answer", "Under the line on the bench, type the number you worked out yourself and tap “Mark it”. A right number gets a tick. For a wrong one StoichPath works the line again with one change at a time (the mole ratio upside down or left out, a start from the reactant that is left over, another substance’s molar mass, a line that stops early, a decimal point that moved) and, when one of them gives your number, names it and draws your line with that factor circled. If none fits, it says so and names nothing. Practice does the same under a wrong typed answer."),
  ("Gas at a temperature and pressure", "A gas volume normally uses the molar volume chosen in Settings. When a question states a temperature and a pressure, choose “Temperature and pressure” in the amount sheet, or tap the conditions under the line when the answer is a volume. One mole then takes R·T ÷ P litres. The problem reader picks these up from the text (°C or K; atm, kPa, bar, mmHg).")),
 "de": ("Zuletzt aktualisiert am 14. November 2026",
  ("Das eigene Ergebnis prüfen", "Tipp unter der Zeile auf dem Labortisch die Zahl ein, die du selbst ausgerechnet hast, und tippe auf „Korrigieren“. Eine richtige Zahl bekommt einen Haken. Bei einer falschen rechnet StoichPath die Zeile mit je einer Änderung noch einmal (Molverhältnis umgedreht oder vergessen, Start beim Edukt, das übrig bleibt, molare Masse eines anderen Stoffs, zu früh aufgehört, verrutschtes Komma), und wenn eine davon deine Zahl ergibt, benennt es den Fehler und zeichnet deine Zeile mit dem eingekreisten Faktor. Passt keine, sagt es das und benennt nichts. Beim Üben geschieht dasselbe unter einer falsch eingetippten Antwort."),
  ("Gas bei Temperatur und Druck", "Ein Gasvolumen nutzt normalerweise das in den Einstellungen gewählte Molvolumen. Nennt eine Aufgabe Temperatur und Druck, wähle im Mengenblatt „Temperatur und Druck“ oder tippe unter der Zeile auf die Bedingungen, wenn das Ergebnis ein Volumen ist. Ein Mol nimmt dann R·T ÷ p Liter ein. Der Aufgabenleser übernimmt diese Angaben aus dem Text (°C oder K; atm, kPa, bar, mmHg).")),
 "fr": ("Dernière mise à jour le 14 novembre 2026",
  ("Corriger sa propre réponse", "Sous la ligne de la paillasse, saisis le nombre que tu as calculé toi-même et touche « Corriger ». Un nombre juste est coché. Pour un nombre faux, StoichPath refait la ligne en changeant une chose à la fois (rapport molaire inversé ou oublié, départ du réactif en excès, masse molaire d’une autre substance, ligne arrêtée trop tôt, virgule déplacée) et, si l’une d’elles donne ton nombre, il nomme l’erreur et redessine ta ligne avec ce facteur entouré. Si aucune ne convient, il le dit et ne nomme rien. Les exercices font de même sous une réponse fausse."),
  ("Gaz à une température et une pression", "Un volume de gaz utilise normalement le volume molaire choisi dans les Réglages. Quand un énoncé donne une température et une pression, choisis « Température et pression » dans la feuille de quantité, ou touche les conditions sous la ligne quand la réponse est un volume. Une mole occupe alors R·T ÷ P litres. Le lecteur d’énoncés les reprend dans le texte (°C ou K ; atm, kPa, bar, mmHg).")),
 "es": ("Última actualización: 14 de noviembre de 2026",
  ("Corregir tu propia respuesta", "Bajo la línea de la mesa, escribe el número que calculaste por tu cuenta y toca «Corregir». Un número correcto recibe una marca. Si es incorrecto, StoichPath rehace la línea cambiando una sola cosa cada vez (relación molar invertida u olvidada, empezar por el reactivo que sobra, masa molar de otra sustancia, línea que se queda corta, coma desplazada) y, cuando una de ellas da tu número, nombra el error y dibuja tu línea con ese factor rodeado. Si ninguna encaja, lo dice y no nombra nada. La práctica hace lo mismo bajo una respuesta incorrecta."),
  ("Gas a una temperatura y una presión", "Un volumen de gas usa normalmente el volumen molar elegido en Ajustes. Cuando un problema da una temperatura y una presión, elige «Temperatura y presión» en la hoja de cantidad, o toca las condiciones bajo la línea cuando la respuesta es un volumen. Un mol ocupa entonces R·T ÷ P litros. El lector de problemas las toma del texto (°C o K; atm, kPa, bar, mmHg).")),
 "it": ("Ultimo aggiornamento: 14 novembre 2026",
  ("Correggere la propria risposta", "Sotto la riga del banco scrivi il numero che hai calcolato da solo e tocca «Correggi». Un numero giusto riceve una spunta. Se è sbagliato, StoichPath rifà la riga cambiando una cosa alla volta (rapporto molare capovolto o dimenticato, partenza dal reagente che avanza, massa molare di un’altra sostanza, riga fermata troppo presto, virgola spostata) e, quando una di queste dà il tuo numero, dà un nome all’errore e ridisegna la tua riga con quel fattore cerchiato. Se nessuna corrisponde, lo dice e non dà nomi. Gli esercizi fanno lo stesso sotto una risposta sbagliata."),
  ("Gas a una temperatura e una pressione", "Un volume di gas usa di norma il volume molare scelto nelle Impostazioni. Quando un problema indica temperatura e pressione, scegli «Temperatura e pressione» nel foglio della quantità, oppure tocca le condizioni sotto la riga quando la risposta è un volume. Una mole occupa allora R·T ÷ P litri. Il lettore di problemi le ricava dal testo (°C o K; atm, kPa, bar, mmHg).")),
 "pt-BR": ("Última atualização: 14 de novembro de 2026",
  ("Corrigir a sua própria resposta", "Abaixo da linha na bancada, digite o número que você calculou e toque em “Corrigir”. Um número certo ganha um visto. Se estiver errado, o StoichPath refaz a linha mudando uma coisa de cada vez (razão molar invertida ou esquecida, início pelo reagente que sobra, massa molar de outra substância, linha que para cedo demais, vírgula fora do lugar) e, quando uma delas dá o seu número, nomeia o erro e redesenha a sua linha com esse fator circulado. Se nenhuma servir, ele diz isso e não nomeia nada. A prática faz o mesmo abaixo de uma resposta errada."),
  ("Gás a uma temperatura e uma pressão", "Um volume de gás normalmente usa o volume molar escolhido nos Ajustes. Quando um problema informa temperatura e pressão, escolha “Temperatura e pressão” na folha de quantidade, ou toque nas condições abaixo da linha quando a resposta for um volume. Um mol ocupa então R·T ÷ P litros. O leitor de problemas tira esses valores do texto (°C ou K; atm, kPa, bar, mmHg).")),
 "nl": ("Laatst bijgewerkt op 14 november 2026",
  ("Je eigen antwoord nakijken", "Typ onder de regel op de werkbank het getal dat je zelf hebt uitgerekend en tik op ‘Nakijken’. Een goed getal krijgt een vinkje. Bij een fout getal rekent StoichPath de regel opnieuw door met telkens één ding anders (molverhouding omgekeerd of vergeten, begonnen bij de stof die overblijft, molaire massa van een andere stof, te vroeg gestopt, verschoven komma) en als een daarvan jouw getal geeft, benoemt het de fout en tekent het jouw regel met die factor omcirkeld. Past er geen, dan zegt het dat en benoemt het niets. Oefenen doet hetzelfde onder een fout antwoord."),
  ("Gas bij een temperatuur en druk", "Een gasvolume gebruikt normaal het molaire volume uit Instellingen. Geeft een opgave een temperatuur en een druk, kies dan ‘Temperatuur en druk’ in het hoeveelheidsblad, of tik op de omstandigheden onder de regel als het antwoord een volume is. Eén mol neemt dan R·T ÷ p liter in. De opgavelezer haalt ze uit de tekst (°C of K; atm, kPa, bar, mmHg).")),
 "ja": ("最終更新：2026年11月14日",
  ("自分の答えを採点する", "実験台の式の下に、自分で求めた数値を入力して「採点する」をタップします。合っていればチェックが付きます。違っている場合、StoichPath は式を一か所ずつ変えて計算し直し（モル比が逆・抜けている、余る反応物から始めた、別の物質のモル質量を使った、途中で止まった、小数点がずれた）、あなたの数値と一致するものがあれば、その原因を示し、該当する換算係数を丸で囲んであなたの式を描き直します。どれにも当てはまらなければ、そう伝えるだけで原因は付けません。練習でも、数値を間違えたときに同じ表示が出ます。"),
  ("温度と圧力を指定した気体", "気体の体積は通常、設定で選んだモル体積で計算します。問題に温度と圧力が書かれている場合は、量の入力シートで「温度と圧力」を選ぶか、答えが体積のときは式の下の条件をタップします。このとき気体 1 mol の体積は R·T ÷ P リットルです。問題の読み取りでも本文から読み取ります（°C または K、atm・kPa・bar・mmHg）。")),
 "ko": ("마지막 업데이트: 2026년 11월 14일",
  ("내 답 채점하기", "실험대의 식 아래에 직접 구한 값을 입력하고 ‘채점하기’를 누릅니다. 맞으면 체크 표시가 붙습니다. 틀리면 StoichPath가 식을 한 군데씩 바꿔 다시 계산해 보고(몰비를 뒤집거나 빠뜨림, 남는 반응물에서 시작, 다른 물질의 몰 질량 사용, 중간에서 멈춤, 소수점 자리 어긋남) 그중 하나가 입력한 값과 일치하면 그 실수를 짚어 주고, 해당 인자에 동그라미를 쳐서 내 식을 다시 그려 줍니다. 맞는 것이 없으면 그렇다고만 알리고 이름을 붙이지 않습니다. 연습에서도 틀린 값을 입력하면 같은 안내가 나옵니다."),
  ("온도와 압력이 주어진 기체", "기체의 부피는 보통 설정에서 고른 몰 부피로 계산합니다. 문제에 온도와 압력이 나와 있으면 양 입력 시트에서 ‘온도와 압력’을 고르거나, 답이 부피일 때 식 아래의 조건을 누릅니다. 이때 기체 1몰의 부피는 R·T ÷ P 리터입니다. 문제 읽기도 본문에서 이를 읽어 옵니다(°C 또는 K, atm·kPa·bar·mmHg).")),
 "zh-Hans": ("最后更新：2026 年 11 月 14 日",
  ("批改你自己的答案", "在实验台换算式的下方输入你自己算出的数值，然后轻点“批改”。算对了会打勾。算错了，StoichPath 会每次只改一处重新计算（摩尔比写反或漏掉、从有剩余的反应物算起、用了别的物质的摩尔质量、没有算完、小数点移位），只要其中一种正好得出你的数值，就指出这种失误，并把你的换算式重画出来、圈出那个因子。都对不上时只会如实告知，不会硬安原因。练习中输错数值时也是这样。"),
  ("指定温度和压强的气体", "气体体积通常按“设置”里选定的摩尔体积计算。题目给出温度和压强时，在用量面板里选择“温度和压强”；答案是体积时，轻点换算式下方的条件。这时 1 摩尔气体占 R·T ÷ P 升。读题功能也会从题目文字中读出这些条件（°C 或 K；atm、kPa、bar、mmHg）。")),
 "ru": ("Обновлено 14 ноября 2026 г.",
  ("Проверка своего ответа", "Под строкой на столе введите число, которое получили сами, и нажмите «Проверить». Верное число получает галочку. Если оно неверно, StoichPath пересчитывает строку, меняя каждый раз что-то одно (мольное отношение перевёрнуто или пропущено, расчёт начат с реагента в избытке, взята молярная масса другого вещества, строка оборвана раньше времени, сдвинута запятая), и, если один из вариантов даёт ваше число, называет ошибку и рисует вашу строку с обведённым множителем. Если ни один не подходит, приложение так и сообщает и ничего не называет. В практике то же самое происходит под неверно введённым ответом."),
  ("Газ при заданных температуре и давлении", "Обычно объём газа считается по молярному объёму, выбранному в настройках. Если в задаче указаны температура и давление, выберите «Температура и давление» на листе количества или нажмите на условия под строкой, когда ответ — объём. Тогда один моль занимает R·T ÷ P литров. При чтении задачи эти условия берутся из текста (°C или K; atm, kPa, bar, mmHg).")),
 "tr": ("Son güncelleme: 14 Kasım 2026",
  ("Kendi cevabını kontrol etmek", "Tezgâhtaki satırın altına kendi bulduğun sayıyı yaz ve “Kontrol et”e dokun. Doğru sayı onay işareti alır. Yanlışsa StoichPath satırı her seferinde tek bir şeyi değiştirerek yeniden hesaplar (mol oranı ters ya da eksik, artan tepkenden başlanmış, başka maddenin mol kütlesi, erken biten satır, kaymış virgül); bunlardan biri senin sayını veriyorsa hatanın adını koyar ve o çarpanı halkaya alarak satırını yeniden çizer. Hiçbiri uymuyorsa bunu söyler, ad koymaz. Alıştırmada yanlış yazılan cevabın altında da aynısı olur."),
  ("Sıcaklığı ve basıncı verilen gaz", "Gaz hacmi normalde Ayarlar’da seçilen mol hacmiyle hesaplanır. Soru bir sıcaklık ve basınç veriyorsa miktar sayfasında “Sıcaklık ve basınç”ı seç ya da cevap bir hacimse satırın altındaki koşula dokun. O zaman bir mol gaz R·T ÷ P litre yer kaplar. Problem okuyucu bu değerleri metinden alır (°C ya da K; atm, kPa, bar, mmHg).")),
}

for lang, (updated, mark, gas) in T.items():
    page = D["pages"][lang]
    page["updated"] = updated
    sections = page["support"]["sections"]
    titles = [s[0] for s in sections]
    if mark[0] not in titles:
        assert len(sections) == 9, (lang, len(sections))
        sections.insert(4, list(mark))      # after "Working backwards"
        sections.insert(7, list(gas))       # after "Amounts"
P.write_text(json.dumps(D, ensure_ascii=False, indent=1) + "\n")
print("ok", {l: len(D["pages"][l]["support"]["sections"]) for l in T})
