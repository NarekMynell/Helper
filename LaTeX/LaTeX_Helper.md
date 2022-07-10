install անելու համար պետքա ներբեռնել MikTeX-ը միայն ադմինիստրատրի համար և perl-ը powershell-ի հետևյալ քմանդով․ & $([scriptblock]::Create((New-Object Net.WebClient).DownloadString('https://platform.activestate.com/dl/cli/1111945401.1646563489_pdli01/install-latest.ps1'))) -c'state activate --default Narek-43/Perl-5.34.0-Windows'

* LaTeX-ը չի հանդիսանում WYSIWYG (What You See Is What You Get):
* Ունի թերություն ռեկլամների շիթերի
* это созданная американским математиком и программистом Дональдом Кнутом
* պարագրաֆը դատարկ տողովա, պռաբելների քանակը կապ չունի
* { } $ & # % _ ^ ~ \   քեյ-սիմվոլներ են, սակայն առաջին 7ը կարելի է ստանալ սկբից դնելով \ («backslash»)

* % comment %
* \TeX, \LaTeX и \LaTeXe - կտպեն հունարենը
* \-ից հետո կամ սփեյս կամ սիվոլ՝ ոչ տառ
* \-ից հետո էոմանդի ավարտը հասկացնելու համար կարելիա դնել \ կամ {}
* ֆայլը պետք է սկսվի \documentclass արտահայտությամբ
    * \documentclass{book}
    * \documentclass{article}
    * \documentclass{report} - (нечто среднее между article и book)
    * \documentclass{proc} - для оформления изданий типа «труды конференции»
    * \documentclass{letter}

    * \documentclass[12pt, twocolumn]{article}
* \documentclass - ից հետո քամանդները վերաբերվում են ամբողջ դակումենտին
* \begin{document}
* \end{document}
* \bfseries, \mdseries - հաստ, unհաստ կամ {\bfseries text}
* \slshape, \itshape, \upshape - թեք, թեք, unթեք 

* \section, \section* - սկսել նոր բաժին համարակալված / չհամարակալված
* \parindent=2cm - մի մատ խորքը
* \label{key} - լինկ ենք տալիս (կարա մեկ ռանով չաշխատի)
    * ~\pageref{key} - կտա էջի համարը
    * ref{key} - կտա բաժնի համարը
* $c^2=a^2+b^2$ - Պյութագորասի թեորեմ
* $R^i_{jkl}$ - Համ վերևի համ ներքևի ինդեք
* 2^{x^3} - 2 հարկանի
* \ge** - ≥
* \approx - ≈
* $$
\frac{(a+b)^2}{4}-
\frac{(a-b)^2}{4}=
ab
$$ - կոտորակ
* $$
1+\left(\frac{1}{1-x^{2}}
\right)^3
$$ - Փակագծերով կոտորակ
$\sqrt[3]{x^3}=x$, but
$\sqrt{x^2}=|x|$ - 





## Packages
* **amsfonts** - Մաթեմատիկական բանաձևերի լրացուցիչ շրիֆտներ
* **longtable** - Աղյուսակներ, որոնք զբաղեցնում են մեկից ավելի էջեր