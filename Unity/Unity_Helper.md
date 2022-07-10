 ## Events
* **OnBecameVisible, OnBecameInvisible** - կանչվում են, երբ օբյեկտը հայտնվում կամ անհետանում է տեսախցիկի սպեկտորից
* **OnCollisionEnter, OnTriggerEnter** - կանչվում են, երբ քոլայդերի կամ թրիգերի հպում է տեղի ունեցել
* **OnDestroy** - կանչվում է, երբ օբյեկտը ջնջվում է

## Asynchronous programming
* [AsyncOperation](https://docs.unity3d.com/ScriptReference/AsyncOperation.html)
* [WaitForEndOfFrame
](https://docs.unity3d.com/ScriptReference/WaitForEndOfFrame.html)
* [WaitForFixedUpdate](WaitForFixedUpdate)

#### [DOTS](https://unity.com/dots)
2018-ից ի-վեր յունիթին ստեղծելա սա, որըընարավորությունա տալիս օգտագործել cpu-ի յադեռները

#### [Coroutines](https://docs.unity3d.com/Manual/Coroutines.html)
* **yield** - քորիթինից դուրս գալու մեխանիզմնա
* [WaitForSeconds](WaitForSeconds) - մեթոդա, որը սպասումա արգումենտում տրված ժամաչափով, մինչև քորիթինի հաջորդ մեկնարկը
    > ժամանակի մասշտաբը կարող է տարբերվել իրական ժամանակից, այն որոշվում է [Time.timeScale](https://docs.unity3d.com/ScriptReference/Time-timeScale.html)-ի միջոցով
* [WaitForSecondsRealtime](https://docs.unity3d.com/ScriptReference/WaitForSecondsRealtime.html) - կանգնացնումա քորիթինը իրական մասշտաբի ժամանակով
* [WaitUntil](https://docs.unity3d.com/ScriptReference/WaitUntil.html) - կանգնացնումա քորիթինը մինչև արգումենտում տրված պայմանը ճիշտ կլինի
* [WaitWhile](https://docs.unity3d.com/ScriptReference/WaitWhile.html) - քորիթինը կատարվումա քանի դեռ արգումենտում տրված պայմանը ճիշտա
#### [Invoke](https://www.google.com/search?q=Invoke+unity+events&oq=Invoke+unity+events&aqs=chrome..69i57j0i22i30.9762j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_NVXsYc-VFY3urgSx1qaQBA16)

## Shaders

* Սքրիփթային շեյդերնեը յունիթիում գրվում են հիբրիդային կերպով՝ CG-ով (ստանդարտ ռենդերինգ) և HLSL-ով (Scriptable renderings: URP, HRP)
* **Legacy Shaders** - Հնացած շեյդերների ընտանիք (մոտ 80 օրինակ), որոնց հիմա փոխարինումա **Standard Shader**-ը
* **Diffuse** և **Specular shaders** - Այստեղ կարևոր է հասկացությունների ֆիզիկակական նշանակությունը

## Textures
* **Normal map** - Այս քարտեզի միջոցով օբյեկտին տրվում են մանր դետալների պատկերման հնարավորություն առանց լրացուցիչ վերտեքսների ավելացման
* **MIP mapping** - Թեքսթուրինգի մեթոդա, որը կախված սիտուացիայից օգտագործումա նույն տեքսթուրի տարբեր ռեզոլուշններով քոփիները 
* **Emmision** - Կարգավորում է լույսը, կարող է օբյեկտն նեկայացնել որպես լույսի աղբյուր
* **Glossiness** - Փայլունություն
* **Smoothness** - Հարթություն
* **Roughness** - Կոպտություն։ Սմութնեսի հակառակնա

## Post_Processing
* **Ambient Occlusion** -  մոտավորացնում է ճեղքերի ստվերները՝ նմանակելով այն, ինչ տեղի է ունենում իրական միջավայրում՝ մգացնելով իրար մոտ գտնվող ծալքերը, անցքերը, խաչմերուկները և մակերեսները: Սա ավելի իրատեսական տեսք է տալիս այն օբյեկտներին, որտեղ շրջապատի լույսը արգելափակված է կամ խցանված է:
* **Anti-aliasing** - հարթեցում՝ մեղմացնումա պատկերների եզրերը (երբ թեք գծերը զուբչաստի կտրտված են երևում, էլ չեն երևա)։ Կան տարբեր [ալգորիթմներ](https://gabestore.ru/blog/da-kto-takoj-etot-vash-msaa-i-ssaa)
    * TAA 
    * SSAA կամ FSAA (Տիռանոզավռ) - մեղմացումը կատարվումա նախքան  սցենայի կառուցումը։ Սկզբից նկարների ռեզոլուշնը մեծանումը 2, 4 կամ 8 անգամ, հետո նորից փոքրանումա սկզբնականի
    * MSAA - սա ի տարբերություն SSAA-ի իսխոդնի նկարին չի կպնում ու ավելի քիչ նագռուզկայա առաջացնում GPU-ի վրա․ օրինակ՝ 8х MSAA - ի նագռուզկեն ավելի քիչա քան 4х SSAA-ինը։
    * FXAA - Nvidia-ի ստեղծած ալգորիթմնա, որը գտնումա գույների կտրուկ փոփոխման հատվածները և մեղմացնումա։ Այստեղ սակայն խնդիրա առաջանում հեռու օբյեկտների դեպքում, որոնք մանր են երևում ու ալգորիթմից հետո դժվար են առանձնացվում։ Այս ալգորիթմը բայց ավելի քիչա նագռուզկա ստեղծում, քան MSAA-ն
    * MLAA - Intel-ինա պատկանում ու աշխատումա CPU-ի վրա ոչ թե GPU-ի։ Այն նմանա FXAA-ի պրինցիպին, այն տարբերությամբ, որ նախքան մեղմացումն, այդ հատվածները բաժանումա մանր սեգմենտների և արդեն խառնումա գույները նրանց մեջ։ Ստացված պատկերի որակի առումով՝ 1x FXAA < 1x MLAA < 2x FSAA
    * SMAA - սա FXAA-ի ու MLAA-ի խառնուրդնա։ Աշխատումա MLAA-ի պրինցիպով, սակայն աշխատումա GPU-ի վրա։
    * TXAA - Nvidia-ինա ու MSAA-ի և SMAA-ի խառնուրդնա

## Shaders
* Կան տարբեր տիպի շեյդերներ․
    * Vertex Shaders
    * Fragment shaders
    * Compute Shaders

## Materials
* **myMaterial(HasProperty("My_Property") ** - կստուգի առկայությունը


## Graphic
* 75 Гц, 85 Гц и 144 Гц также распространены для настольных мониторов. Для соревновательной игровой сцены есть еще более высокие частоты обновления. Так что, если ваше приложение может стабильно достигать 85 кадров в секунду, оно будет хорошо работать с VSync на всех дисплеях. Если бы он мог достигать только 60 кадров в секунду, тогда 75 Гц дисплеи упали бы до половины при 37,5 кадрах в секунду, 85 Гц упали бы вдвое до 42,5 кадров в секунду и 144 Гц упали бы до трети при 48 кадрах в секунду. Однако это предполагает постоянную производительность. В действительности частота кадров может колебаться в пределах, кратных частоте обновления.

## Rendering
* [Graphics Performance](https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html)
* **Camera Clipping**
Երբ օբյեկտները, որոնք կամեռայի սպեկտորից դուրս են, ռենդ չեն լինում։ Դեֆոլթով միացվածա։
* **Occlusion Culling**
Երբ օբյեկտները, որոնք ծածկված են այլ օբյեկտներով, ռենդ չլինեն։ Յունիթիում այն իրականացվումա [Umbra](https://docs.unity3d.com/Manual/occlusion-culling-additional-resources.html) գրադարանի միջոցով։ Որպեսզի աշխատի պետքա, որ կամեռայում այն միացված լինի, այնուհետև պետքա մտնել *Window > Rendering > Occlusion Culling* պատուհանը ու տալ bake:
* **Forward and Deferred Rendering**
Forward Rendering-ը նկարումա բոլոր օբյեկտների բոլոր պոլիգոններն ամեն լույսի համար։ Բարդությունը - O(num_geometry_fragments * num_lights)։ Deferred Rendering-ը սկզբից կառուցումա գեոմետրիան, բուֆերնորով ստանում տարբեր մեփերն ու նոր ավելացնում լույսը ամեն պիքսելի համար։ Բարդությունը - O(screen_resolution * num_lights)։ [Տես մանրամսն](https://gamedevelopment.tutsplus.com/articles/forward-rendering-vs-deferred-rendering--gamedev-12342)։
* **Normal map**-ն աշխատումա միայն երբ լույսի ուղիղ ճառագայթներն են ընկնում մակերևույթի վրա
* **Project Setting > Player > Other Settings > GPU Skinning** - Եթե միացնենք, ապա Skined Mesh-ի հաշվարկները կկատարի GPU-ն այլ ոչ CPU-ն

## URP
* URP-ի համար նոր լույսի ավելացումը GPU-ի լրցուցիչ կանչեր չի ստեղծում, քանի որ միավորումա բոլոր լույսերն որպես մեկ ընդհանուր, ի տարբերություն BRP-ի․
* Եթե Game Mode-ի ժամանակ State-ով ստատիստիկան բացենք, ապա կնկատենք որ URP-ի սեթինգսներում batches-ների քանակի մեջ ստվերները չեն մտնում

## Profiler
* [Profiler-ի հիմնական ֆունկցիաները](https://docs.unity3d.com/Manual/profiler-markers.html)

## Components
* **[LOD GROUP](https://docs.unity3d.com/ru/530/Manual/class-LODGroup.html)** - կամեռայի հեռավորությունից կախված փոխումա օբյեկտների դետալիզացիան
* **[Reflection Probes](https://learn.unity.com/tutorial/configuring-reflection-probes-2019-3#)** - երբ օբյեկտի մատերիալին տալիս ենք արտացոլելու հատկություն (smoothness, metalic), այն միևնույն է լավ չի արտացոլոմ շրջակայքի օբյեկտները, այդ խնդիրը լուծումա այս կոմպոնենտը, որը իրենից ներկայացնում է վեցանիստ, որի ներսում գտնվող օբյեկտները արտացոլվում են
* **[Character Controller](https://docs.unity3d.com/Manual/class-CharacterController.html)** - կոմպոնենտի միջոցով կարող ենք սահմանել դիքի մաքսիմալ անկյունը, սանդուղքի մաքսիմալ բարձրությունը, որը խառակծեռը կարա բարձրանա: Այն սակայն գրավիտացիայի չի ենթարկվում, դա կարելիա տալ ռուչնոյ՝ **isGrounded**-ի միոցով
* **EventTriger** - Ավելացնում ենք օբյեկտին ու տարբեր իվենթներ ենք հենդլ անում էտ օբյեկտի հետ կապված

## Packages
* **ProBuilder** - Մոդելավորում անմիջապես յունիթիի մեջ
* **Burst** - Օպտիմիզացիայի մեխանիզմա, որը թույլա տալիս օգտագործել multithreading
* **Game Booster** - Պեքիջա, որտեղ կան բազմաթիվ պատրաստի սքրիփթներ
* **[Cinemachine](https://docs.unity3d.com/Packages/com.unity.cinemachine@2.3/manual/CinemachineOverview.html)** - կամեռայի ֆունկցիոնալա, որը հնարավորությունա տալիս հետևել օբյեկտին տարբեր ռակուրսներից և կառավարել անցումները միմիանց միջև
* **Input System** - Ինփութի ավելի նոր և բազմաֆունկցիոնալ տեխնոլոգիա
* **Tilemap** - Sprite-ը սցենայում դասավորելու հարմար թուլա, [տես՝](https://www.youtube.com/watch?v=DbzH-Z1fbU4&ab_channel=LogFaer)
* [Addressable](https://docs.unity3d.com/Packages/com.unity.addressables@1.19/manual/index.html) - Հնարավորությունա տալիս Asset-ներին տալ Addressable ֆորմատ ու իրենց զագռուզիծ անել ռանթայմ (նաև նեթվորկով):



## Build
* **IL2CPP**-ն դանդաղա բիլդ լինում, սակայն փաբլիշի համար էնա ինչ պետքա, քանի որ սփորթա անում համ ARM-32 համ ARM-64: **Mono**-ն ավելի արագա բիլդ լինում, սակայն փաբլիշի համար չի աշխատի։ Ուստի դևելոփփմենթի ընթացքում ճիշտա օգտագործել Mono-ն, իսկ Փաբլիշ անելուց՝ IL2CPP-ն
* **ADB with WiFi**
    1. Միացնել դիվայսը debug ռեժիմով USB-ով
    2. Տերմինալում գրել ```adb tcpip 5555```
    3. ```adb connect <you'r devices IP adress>``` ip-ն հնարավորա տեսնել դիվայսի սեթինգներում
    4. ```adb devices``` ցույց կտա մացված դիվայսները։ Եթե գրած լինի ```<you'r devices IP adress>    device```, ապա WiFi-ով միացումը կատարվածա, կարող ենք անջատել USB-ն

    ```adb kill-server```
    
    ```adb start-server```

## Tutorials
* [3D ժելե](https://www.youtube.com/watch?v=Kwh4TkQqqf8&ab_channel=UnityCity) - using sprite shape
* [2D ժելե](https://www.youtube.com/watch?v=F82BlnW5z6g&ab_channel=LoneX) - using script
* [Ջրի էֆֆեկտ օդում](https://www.youtube.com/watch?v=3CcWus6d_B8&ab_channel=ABitOfGameDev) - using shader graph




## Օգտակար
* [Asset Bundles](https://learn.unity.com/tutorial/introduction-to-asset-bundles#) - Կոնտենտա, որը պահվումա ապլիքեյշնից առանձին ու թույլա տալիս ներբեռնել (լոկալ կամ ինտերնետից) ու օգտագործել ռանթայմ: 2018-ից ներքև սրա իմպլեմենտացիայի համար օգտագործվումա *Asset Bundles Manager*-ը, իսկ այժմ՝ [Addressables](https://docs.unity3d.com/Packages/com.unity.addressables@1.19/manual/index.html)-ը։
* [Multiplayer and Networking](https://docs.unity3d.com/Manual/UNet.html)
* **Billboard** - LOD-ի նման բանա, որը 3D օբյեկտները հեռավորությունից կախված դարձնումա 2D: Այս մեխանիզմի մեկ այլ գործածումա 2D օբյեկտների պտույտով 3D-ի իմիտացիա ստեղծելը, [տես՝](https://www.youtube.com/watch?v=_LRZcmX_xw0&ab_channel=gamesplusjames)
* **Global illumination** - Լույսի արտացուլումնա



## Best Practic
* [Հատուկ ֆոլդրներ](https://docs.unity3d.com/Manual/SpecialFolders.html)
    * Resources
    Այս ֆոլդրի կամայական ֆայլ գնումա բիլդ, անկախ նրանից *Resources* ֆոլդըրը հիրարխիայում որտեղա գտնվում քանի հատ կա: TextMeshPro-ն օգտագործումա էտ ֆոլդըրը, ինչը լավ չի։
    * Editor
    Այս ֆոլդրի մեջ գտնվող սքրիփթները բիլդ չեն գնում։ Ֆոլդրից կարա մեկից ավել լինի հերարխիայի կամայական վայրում։
* [AssetPost Processor](https://docs.unity3d.com/ScriptReference/AssetPostprocessor.html)
Քլասսա էդիթրի համար, որը օգտագործվումա ասսեթների իմփորթների ժամանակ։ Կարանք գործողություններ սահմանենք իմփորթ լինող ասսեթների համար, որոնք ավտոմատ կկատարվեն։
* **Use Sprite Atlas**
Sprite Atlas-ը նվազեցնումա daw call-երն՝ ամեն ատլասի համար օգտագործելով 1 քոլ։ Այն րոթեյշնի շնորհիվ նաև հնարավորությունա տալիս հնարավորինս պլոտնի դասավորել սփրայթները՝ խնայելով թափանցիկ պիքսելների համար։
Օրինակ UI-ում այն օգտագործելու համար կարող ենք ստեղծել հետևյալ սքրիպթը ու այն տանք բոլոր Image պարունակող այթըմներին։
    ~~~C#
    using UnityEngine;
    using UnityEngine.U2D;
    using UnityEngine.UI;

    [ExecuteInEditMode]
    public class AtlasSprite : MonoBehaviour
    {
        [SerializeField] private SpriteAtlas spriteAtlas;
        [SerializeField] private string spriteName;

        private void Start()
        {
            GetComponent<Image>().sprite = spriteAtlas.GetSprite(spriteName);
        }
    }
    ~~~
* **[Use Object Pooling](https://learn.unity.com/tutorial/introduction-to-object-pooling#)**
Սա Դիզայն Փաթերնա, որի համաձայն ամեն անգամ նոր օբյեկտներ ստեղծելու ու ջնջելու փոխարեն, նախապես ստեղծում ենք անհրաժեշտ քանակով ու պռոստը միացնում/անջատում։ Սրա շնորհիվ չենք ծանրաբեռնում մեր GC-ին ու CPU-ին։
* **Չօգտագործել Invoke և SendMessage**, դրա փոխարեն օգտագործել *Coroutines*
* **Օգտագործել assertions**
* **Հնարավորինս զերծ մնալ GameObject.Find();**-ից, այն շատ դանդաղ է
* **Update-ում չկանչել GetComponent ֆունկցիան**, փոխարենը Start-ում կանչել ու պահել փոփոխականում
* **Չվստահել OnDestroy/OnTriggerExit ֆունկցիաներին** - Օրինակ եթե օբյեկտները ակտիվ չլինեն, էտ ֆունկցիաները կարող են չկանչվել
* **Use Unity Job System and Burst compiler for multithreading and high performance**:

