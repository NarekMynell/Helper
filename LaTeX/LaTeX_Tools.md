## Դիստրիբյուտորներ (distributors)

<br>

### Windows
Windows ՕՀ-ում LaTeX-ի դիստրիբյուտոր կարող են ծառայել [MiKTeX](https://miktex.org/)-ը, [proTeXt](http://www.tug.org/protext/) կամ [TeX Live](http://www.tug.org/texlive/)-ը։ Վերջիններս իրենց մեջ ներառում են TeX-ի համակարգը, ներառյալ LaTeX-ը և խմբագրիչ՝ փաստաթղթերի կառուցման համար։

<br>

### Mac OS
Mac OS-ի դիստրիբյուտորն է [MacTeX](http://www.tug.org/mactex/)-ը, որն իր մեջ ներառում է TeX-ի համակարգը, ներառյալ LaTeX-ը և խմբագրիչ՝ փաստաթղթերի կառուցման համար։

<br>

### Linux

Linux ՕՀ-ի դիստրիբյուտորն է [TeX Live](https://www.tug.org/texlive/)-ը, որը փոխարինում է արդեն չսպասարկվող teTeX-ին։ TeX Live-ն իր մեջ ներառում է TeX-ի համակարգը, ներառյալ LaTeX-ը և խմբագրիչ՝ փաստաթղթերի կառուցման համար։

<br>

## Խմբագրիչներ (editors)

Ստորև ներկայացված են TeX (LaTeX)-ի առավել տարածված խմբագրիչները: 

<br>

### Բազմապլատվորմ (cross-platform) խմբագրիչներ

* [TeXmaker](https://www.xm1math.net/texmaker/)
* [Kite](https://www.kite.com/)
* [TeXstudio](https://www.texstudio.org/)
* [MikTex](https://miktex.org/)
* [Emacs](https://www.gnu.org/software/emacs/)
* [LyX](https://www.lyx.org/)
* [AUCTeX](https://www.gnu.org/software/auctex/)
* [VS Code](https://code.visualstudio.com/)-ն [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) ընդլայնումով (extension)

<br>

### Առցանց խմբագրիչներ
* [Overleaf](https://www.overleaf.com/)
* [Papeeria](https://papeeria.com/)
* [LaTeX Base](https://latexbase.com/)
* [Authorea](https://www.authorea.com/)

<br>

Խմբագրիչների միջև համեմատություններին կարելի է ծանոթանալ հետևյալ հղումներով.
* [հղում 1](https://en.wikipedia.org/wiki/Comparison_of_TeX_editors)
* [հղում 2](https://ru.wikipedia.org/wiki/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%BE%D0%B2_TeX)
* [հղում 3](https://360wiki.ru/wiki/Comparison_of_TeX_editors)

<br>

## Փաթեթներ (packages)

Ստանդարտ դիստրիբյուտորներն ընդգրկում են հիմնական փաթեթները, սակայն կան շատ փաթեթներ, որոնք ներառված չեն դրանց մեջ։ [CTAN](https://www.ctan.org/pkg) կայքում հնարավոր է տեսնել բոլոր փաթեթները, ծանոթանալ դրանց հետ և ներբեռնել։ Ներբեռնած փաթեթները գործածելու համար պետք է դրանք տեղադրել համապատասխան թղթապանակում։ Փաթեթների կառավարման համար կան նաև մի շարք ծրագրեր([TeX Live Utility](https://www.macupdate.com/app/mac/58685/tex-live-utility), [MikTeX Console](https://miktex.org/howto/miktex-console)), որոնց միջոցով հնարավոր է տեսնել առկա և ոչ առկա փաթեթները, հասանելի թարմացումները, տեղադրել և հեռացնել դրանք։

<br>

## Կազմիչներ (compilers)

Գոյություն ունեն LaTeX-ի փաստաթղթերի 4 կազմիչներ՝ [LaTeX](#latex), [pdfLaTeX](#lualatex), [XeLaTeX](#xelatex) և [LuaLaTeX](#lualatex): Փաստաթղթերը կարող են թարգմանվել վերոնշվածներից որևէ մեկով։ Խմբագրիչները հիմնականում տալիս են կազմիչի ընտրության հնարավորություն, սակայն դա հնարավոր է նաև իրականացնել «կախարդական մեկնաբանությունների» միջոցով։ Դրա համար հարկավոր է փաստաթղթի սկզբում ավելացներ հետևյալ հրամաններից որևէ մեկը.

* `% !TeX program = latex`
* `% !TeX program = pdflatex`
* `% !TeX program = xelatex`
* `% !TeX program = lualatex`

Հիշեցնենք, որ լռելյայն կազմիչը pdfLaTeX-ն է։<br> 
Փաթեթները շատ դեպքերում հասանելի չեն լինում բոլոր կազմիչների համար։<br>
Ստորև ներկայացված են կազմիչների առանձնահատկությունները։

### LaTeX

Այն *LaTeX* ֆայլից նախքան *PDF* ստանալը, փոխակերպում է միջանկայլ *DVI* ֆայլի։ LaTeX կազմիչը Հնարավորություն է տալիս աշխատել միայն *.eps* և *.ps* գրաֆիկական ձևաչափերի հետ։

### pdfLaTeX

[pdfLaTeX](http://www.tug.org/applications/pdftex/)-ը TeX-ի ընդլայնված տարբերակն է, որի մեջ ներառված է eTeX ընդլայնումը։  Այն *LaTeX* ֆայլն անմիջապես փոխակերպում է *PDF*-ի։ Հնարավորություն է տալիս աշխատել *.png*, *.jpg*, *.pdf* գրաֆիկական ձևաչափերի հետ։ pdfLaTeX-ն օգտագործում է ASCII կոդավորման համակարկն և ունի սահմանափակ հնարավորություններ աշխատելու [OpenType](https://www.adobe.com/products/type/opentype.html) տառատեսակների հետ, ուստի կիրառելի լուծում է լատինատառ փաստաթղթերի պատրաստման համար, որոնք չեն պահանջում բազմաբնույթ սիմվոլների օգտագործում։

### XeLaTeX

[XeLaTeX](http://tug.org/xetex/)-ը Հնարավորություն է տալիս աշխատել *.png*, *.jpg*, *.pdf* և *.eps* գրաֆիկական ձևաչափերի հետ։ Աշխատում է UTF-8 կոդավորման համակարգով, ուստի կիրառելի լուծում է ոչ լատինատառ տեքստերի հետ աշխատելիս։ XeLaTeX-ը տալիս հնարավորություն աշխատելու գրաֆիկական պատկերներ ապահովող [pstricks](https://www.ctan.org/pkg/pstricks-base) փաթեթի հետ։

### LuaLaTeX

[LuaLaTeX](http://www.luatex.org/)-ը pdfLaTeX-ի ընդլայնված տարբերակն է, որը հնարավորություն ունի անմիջապես *LaTeX* ֆայլում կազմել սցենարներ [Lua](https://www.lua.org/) լեզվով։ LuaLaTeX-ը հնարավորություն է տալիս աշխատել .png, .jpg, .pdf և .eps գրաֆիկական ձևաչափերի հետ։ Այն աշխատում է UTF-8 կոդավորման համակարգով, ուստի կիրառելի լուծում է ոչ լատինատառ փաստաթղթերի հետ աշխատելիս։ Սակայն երբ կարիք չկա սցենարներ կազմելու, ապա LuaLaTeX-ի փոխարեն կարելի է օգտագործել XeLaTeX-ը։
