get info about command
git name -h
git help name

```ctrl + l```  - maqruma terminaly
```ctrl + c```  - ognuma anelaneli vichakum

* ```git --version``` - tpuma giti versian
```:q``` - ognuma anelaneli vichakum

-----------------------------------------------------------

* ```git reset``` - maqruma terminali exacy
* ```git reset filename``` - orinak yete tvel enq add filename u poshmanel
* ```git reset .``` - bolor stage exac filery darcnuma karmir
* ```git reset .idea``` - unstagea anum
* ```git reset --hard``` - երբ գնում ենք անցյալի քոմիթ (detached head վիճակ), բացում ենք նոր բրենչ, ինչ-որ չենջեր ենք անում հետո ուզում ենա ատմենիծ անենք

-----------------------------------------------------------

```ll``` - asuma te inj fayler kan baci hidddenneric
```ls -al``` - listov tpuma bolor faylery ayd tvum hiddenery
* ```git ls-files``` - tpuma commit arac filery

-----------------------------------------------------------

* ```git init name``` - stexcuma(yete chka) name folder u avelacnuma dranum git repository
```cd name``` - mtnuma name folder u arden koxqy gruma branchi anuny , yete chi grum uremn et papkayum git repo chka avelacrac
```cd ..``` - folderov heta gnum
```cd -``` - folderov heta gnum verjin ekacd texd

-----------------------------------------------------------

* ```git add fileName``` - asum em vor es fayly hishi (stage-a anum)
* ```git add -u``` - stagea anum TRACK arac popoxvac faylery voronq karmirov ein
* ```git add .``` - current diri amboxj parunakutyuny add-a anum
* ```git add -A``` - amboxj projecti exacy add-a anum

-----------------------------------------------------------

* ```git commit -m "Task-N"``` - sranov asum enq vor TRACK ani add arac faylery  
* ```git commit``` - karanq senc aranc argumenti grel u ardyunqum kbacvi VIM editory u kspasi massagei:   ```i``` enq sexmum vor insert anenq u grum enq commiti massegen heto sexmum enq ```esq``` u ```:wq``` isk aranc commit aanelu durs galu hamar parzapes ```:q``` 
* ```git commit -a -m "..."``` - commita anum miagamic aranc stage anelu, bayc sa ignora anum ayn faylery foronq track arvac chen exel, toist nor en
* ```git commit --amend``` - Ապդեյթա անումա քմիթն ու ավելացնում սթեջ արած չենջերը

-----------------------------------------------------------

* ```git status``` - cuyca talis te vor faylerna hishum u voronc shan tex chi dnum (commitic heto el piti hishelu ban chunena)
                               nayev asuma te hishvox fayleric voroncum en popoxutyunner exel

* ```git diff``` - cuyca talis te inj popoxutyunner en exel hishvox faylerum
* ```git diff file1``` - cuyca talis miayn ays faylum exac popoxutyunnery
* ```git diff branch1``` - yntacik branchy khamemati branch1-i het
* ```git diff branch1 --stat``` - statistikaya popoxman masin
* ```git diff commitID1``` - cuyc kta tarberutyuny commitID1-i nkatmamb 

-----------------------------------------------------------

* ```git log``` - tpuma commitneri logy
* ```git log -3``` - ktpi verjin 3 commitnery   
* ```git log --oneline``` - ktpi aveli kompakt :)
* ```git log branch1 --oneline``` - ktpi miayn branch1-i commitnery
* ```git show --pretty=fuler``` - ktpi aveli manramasn
* ```git show ID1``` - ktpi ID1 commiti manramasnery
* ```git show HEAD~~``` - ktpi HEAD commitic 2 commit het commity
* ```git show HEAD~2``` - ktpi 2 commit hety
* ```git show @-3``` - @==HEAD
* ```git show branch1~:file1``` - ktpi branch1-i naxord commiti file1 fayly
* ```git show :/inchvorBar``` - ktpi ayn commity, vori anvan mej ka nshvac bary (yete  shat ka , ktpi amenatarmy)

-----------------------------------------------------------

* ```cat fileName``` - tpuma fayly
* ```cat f1 > f2``` - f1-i exacy qcuma f2-i mej
* ```cat file1 | less``` - yerb fayli parunakutyuny shat meca, ba vuma mec patuhan vory karavarum enq probelov,p u q taerov
* ```vim fileName``` - bacuma fyaly popoxelu hamar

-----------------------------------------------------------

* ```git branch TASK-N``` - stexcum enq TASK-3 chyuxy
* ```git branch -d TASK-1``` - kjnji TASK-1 branchy
* ```git branch -m TASK-2``` - kpoxi yntacik branchi anuny
* ```git branch``` - ktpi yntaciq branchi anuny
* ```git branch -v``` - ktpi branchneri anunnery yev commitneri ID-nery
* ```git branch -f name1 ID1``` - kstexci name1 branchy (yete chka) u iran ktani ID1 commiti vra, isk yete dranic heto commitnera unecel, apa kjnji dranq
* ```git branch -f b1 b2``` - asum enq vor b1-y cuyc ta ayntex vortex b2-na

-----------------------------------------------------------

* ```git checkout TASK-N``` - gnum enq et chyux
* ```git checkout -b TASK-1``` - stexcuma branchy u miangamic checkout linum vran
* ```git checkout -B name1 ID1``` - kstexci(yete chka) name1 branchy u nran ktani ID1 commiti vra
* ```git checkout fileName``` - heta berum popoxvac filename fayli naxkin tesqy (stage charac)
* ```git checkout .``` - heta berum bolor popoxvac fayleri naxkin tesqy (stage charac)
* ```git checkout commitID1``` - mez kberi commitID1 ID-ov commiti vichakin
* ```git checkout -f ...``` - yerb inj vor branchum enq yev uzum enq gnal ayl branch, bayc unenq kisat toxac gorc apa forceov sax et isat toxac gorcery jnjum enq u gnum :(
* ```git checkout -f HEAD``` - kgang  branchi verjin commiti vijakin` jnjelov arvac popoxutyunnery 
* ```git checkout ID1``` - ∎∎∎∎ kgna ayd commiti vra, BAYC et commity karoxa parunakvi mi qani branchneri hamar u ardyunqum senc checkoutov gity gnuma ktrvac commiti vijaki, aysinqn chi gtnvum vochmi branchi vraa, u yete commit anenq, et commity kmna odum kaxvac :(
git checkout ID1 file1 - yete uzum enq unenanq fali et commiti vijaky, apa senc fayli et vichaky kga u stage klini
* ```git checkout -- master``` - yet master anunov fayl ka, apa gity kgna voch t ayd fayli vra ayl branchi, dra hamar -- enq dnum vor haskana fayla

-----------------------------------------------------------

* ```git cherry-pick ID1``` - commity coppya anum current branchi vra

* ```git stash``` - arxivaci kani ira mej arvac popoxutyunnery u kheracni ayn
* ```git stash pop``` - het keri ayd arxivacia arvac popoxutyunnery

-----------------------------------------------------------

* ```git merge B1``` - current branchin kmiacni B1 branchy u kberi verjinis vijakin; Irakanum voch te B1-i faylerna berum lcnum currenti mej, ayl curreni cucichin veragruma B1-i cucichy isk yete uzum enq het berenq eli naxkin vijakin, apa naxkin ID-n pahpanvuma .git/ORIG_HEAD faylum u karanq grenq.' git branch -f master ORIG_HEAD

* ```git rm -r MyDir``` - "-r" yete repo e ayl voch file:  git rm = rm + add
* ```git rm -f file``` - force removing: when git get warning about removing non-saved changed file
* ```git rm --cached file``` - for removing in index
* ```git mv a.txt b.txt``` - remove a to b, and to stage this changes

-----------------------------------------------------------

* karanq bacenq ```.gitignore``` filey u grenq mer uzac ignor linox faylery
   ~~~bash
         *.log - ignore kani bolor ".log" filery
         *.py[co] - ignore kani ".pyc" yev ".pyo" filery 
         yy-4[0-9]* - ignore kani orinak "yy-43.xx" fayly
         *.py? - ignore kani or ".pyl" fayly
         MyDir/ - ignore kani "MyDir" directorynery bayc voch filery
         /MyDir/ - ignore kani miayn kornivaya et anunov foldery
         a/b - ignore a/b, NOT c/a/b
         doc/*.html - doc/file.html, NOT aa/doc/file.html
         /*.txt - t.tx, NOT a/t.txt
         var/www*/tmp - var/wwwttt/tmp, NOT var/www/info/tmp
         users/*/private - NOT users/private, users/a/b/private
         ```/*.log - same as *.log
         ```/a/b - c/a/b, f/h/h/j/a/b

         .*
         !.a
         !.b - ignore kani bolor .xxx-ery baci .a-ic u.b-ic
   ~~~
* ```echo file1 > .gitignore``` - stexcuma .gitignore hatuk fayly u nra mej qcuma mez anpitan file1 fayly
* ```echo file2 >> .gitignore``` - yerb arden .getignore fayly stexcvaca


## Configurations

configurationi 3 tesak ka
1. --local (defoult) - current projecti hamar
2. --global - user-i hamar
3. --system - for all users

* ```git config --list``` - ktpi configuracianery (local)
* ```git config --global --list``` - ktpi configuracianery (global)
* ```git config --global user.name newName``` - global kerpov poxvuma useri anuny, karelia tesnel hajord commitneri logerum
* ```git config --global user.email newEmail``` - paza
* ```git config --global core.autocrlf false``` - anjatuma add-i jamanak bervox worningnery

> ```alias```-nery naxatesvac en commandnery mer uzac dzevov rename anelu hamar, orinakner`
* ```git config alias.st status``` - git status ===> git st (local)
* ```git --global config alias.tt 'config --global --list'``` - git config --global --list ===> git tt (global)
* ```git --system config alias.tpi '!echo "ttu"; echo "tan"'``` - mi qani toxanoc miangamic

* unixum faylery toxery haskacvum en 'LF'('0a')-ov, isk windowsum 'CRLF'('0d 0a')-ov
git core.autocrlf ...... 
* ```.gitattributes``` ֆայլը կարող ենք ստեղծել ռեպոյում, և դրա մեջ տանք քոնֆիգներ։ Սովորական քոնֆիգներից սա տարբերվումա նրանով, որ ամեն դեվելոձեր առաձին չանի (գռֆս)։ Օր․ ```\* text=auto``` համարժեքա * ```git config core.autocrlf input```, սակայն սրանից հետո պետքա կանչել * ```git add --renormalize .``` հրամանը, որ փոփոխությունները թարմացվեն 



## REMOTE REPOSITORY

* ```git pull``` - originic copy enq anum verjin commity
* ```git clone filePath``` - remote repoic clon anelna
* ```git clone A B``` - A_n (A folderi MIJI faylery) clone kani B_um(kstexci B_n yete chka)
* ```git push origin TASK-2``` - mer branchy uxarkum enq remote repo
* ```git push origin HEAD --force``` - Եթե ուզում ենք արած չենջերը միանգամից փոխանցվեն օրիջինին
* Originy da remote repon e  (shared repo)
* pull enq anum directorin heto branch enq arandznacnum dra vra shxatum enq heto 
   push enq anum remote repo heto entex arden createa arvum Pull request kam Merge request
* Pull recuesty yerb menq verjacrel enq mer branchy u myus andamnery karan rewiev anen 
   (comment-moment) bayc merge der chi arvum masteri het
$$$$$$$ nor branchnery misht sarqel master branchic(defoult branchic) yet kariq chka ayli

* add-i jamanak worningnera tpum voronc mej kan CRLF kam LF , dranq hamapatasxanabar Windowsi u Linuxi syntaxnern en
* globalov arac confignery pahvum en user/narek/gitconfig faylum, isk localnery yntaciq directoriyi .git/config faylum
∎ commit anelis inj vor tver en grvum. orinak 100664, stexic 100-y nshanakuma vor fayla commit exel,
  isk 644-y` vor executy priority chuni, (gitin menak et accessna hetaqrqir), isk windowsum qani vor execute
  accessy arandzin chi linum, injpes unixum, apa misht 665-a linelu
∎ patnakanoren gity datark direry chi tesnum, dra hamar sovorabar folderi mej dnum en zroyakan 
  hishoxutyamb ".gitkeep" fayly :)

* ```git push --force``` - Օրիջինում կգրի մեր մոտի եղածը
* ```git reset --hard origin/master``` - Կարելիա ասել թաա կլոն կանի՝ չպահպանելով մեր մոտի չենջերը