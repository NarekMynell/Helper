# Input System
[Turorial](https://www.youtube.com/watch?v=Yjee_e4fICc&ab_channel=CodeMonkey)
Ինփութի նոր և բազմաֆունկցիոնալ տեխնոլոգիա։ Այն հասանելի է փեքիջ մենեջերում
* Ստանդարտ ինփութի կամ ինփութ սիսթեմի ընտրումը կատարվում է՝
    **Edit > Project Settings > Player > Active Input Handling**
* Input-ների դիֆայնները․
    ~~~C#
    ENABLE_INPUT_SYSTEM=1 // միացված է նոր տեխնոլոգիան
    ENABLE_LEGACY_INPUT_MANAGER=1 // միացվաշ է հին տեխնոլոգիան
    ~~~
* Պեքիջի կոդերը **UnityEngine.InputSystem** namespace-ում են, բայց կարա լինի որ իմփորթից հետո էդիթորոին հասանելի կոդերը ապդեյթ չեն եղել․ դրա համար՝
    **Edit > Preferences > External Tools > Registry packages > Regenerate Project Files**
* Input System-ի Asset ստեղծելու համար՝
    **Create > Input Action**

>**Window > Analysis > Input Debug** - Կտա տեղեկատվություն բոլոր միացված սուփփորթ լինող և չլինող ինպութ-սարքերի մասին։ Կարող ենք դաբլ քլիք անել որևե մեկի վրա ու տեսնել բոլոր պարամետրերն, ինչպես նաև կիրառել սարքվուրումն ու տեղում տեսնել արդյունքը

## Input Settings
Edit > Project Settings > Input System Package
Այստեղ պահվում են դեդժֆոլթ պարամետրերը, սակայն կարող ենք նոր ասսետ ստեղծել և մեր ուզած սեթինգսները տալ

## Input Actions Windows
* Վերևի աջ մասում կարող ենք սահմանել ինպութի սարքավորումները։ Մի սարքավորման համար կոդը գրում ենք ու մյուսների համար այլըս կարիք չկա, պարզապես կարգավորում ենք սեթինգսները։ Action բաժնում էվենթը նույննա բոլոր սարքավորումների համար, իսկ նույն Action բաժնի կոնկրետ նպութը(տարբերա ամեն սարքավորման համար)
* Պատուհանն ունի 3 հիմնական բաժիններ,
    * **Action Maps** - օրինակ՝ քայլելը մի մապ կարող ենք սարքել, մեքենա վարելն՝ մի, UI-ն էլ՝ մեկ ուրիշ
    * **Actions** - Կոնկրետ գործողությունը՝ քայլել աջ, ձախ, կրակել ․․․
        * **Binding** - input ավելացնելու համար պետքա սրա վրա սեղմել
    * **Properties**
        * **Action**
            * **Action Type**
                * **Value** - իվենթի ֆունկցիայում ստանում ենք արժեք, ոչ թե տուպը բաթըն
                   * **Control Type** - թե ինչ տիպի արժեք պետքա ստանանք
                    > օրինակ կարող ենք **աջ, ձախ, վերև, ներքև** շարժը սահմանենք՝
                    >Action > Action Type : Value, Control Type : Vector2
                    >Delete Binding > Add 2D Vector Composite
                    >Իսկ սքրիփթում՝ 
                    ~~~C#
                    context.ReadValue<Vector2>()
                    ~~~
                    >Օր՝ update-ում վերջինս ունենալու համար՝
                    ~~~C#
                    myClassObj.myMap.myAction.ReadValue<Vector2>()
                    ~~~
                * **Button** - իվենթի ֆունկցիայում ստանում ենք պռոստը բաթըն
                * **Pass Trough** - նեադնազնաչնսծի համարա, օրինակ եթե մեկից ավելի ինփութի սարքավորումա միաժամանակ աշխատում, ինփութ սիստեմի կոդերը ավելի շատ աշխատանք կկատարեն, բայց բոլոր սարքերի ինփութները միաժամանակ կկատարեն (դժվար պետք գա)
        * **Interactions** - (default: Press) Տալիս ենք սեղմելու ձևը
            * **Hold**
            * **Multi Tap**
            * **Press**
            * **Slow Tap**
            * **Tap**
        * **Processors** - հարմամարա գեյմփադների համար
            * **Stick Deadzone** - շատա լինում, որ գեյմփադների ստիկերն ազատ վիճակում զրո չեն կանգնում, այս պարամետրով կարող ենք մեծացնել 0-ի շրջակայքը և/կամ փոքրացնել 1-ի շրջակայքը
            * **Normalize Vector 2** - ստիքը թեկուզ մի-քիչ էլ թեքենք մեկա վեկտորի մոդուլը մեկ կդարձնի



## Player Input Component
* **Create Action** - Ավտոմատ կստեղծի Input Action ասսեթ արդեն սահմանված ստանդարտ ինփությներով
* **Default Map** - Օրինակ եթե ունենք մեկից ավել map-եր, որոնք օգտագործում են մկնիկի քլիքը, օրինակ Player-ն ու UI-ը, ապա սրանով սահմանում ենք, թե համընկման դեպքում, որը ընդունվի, կոդով կարող ենք փոխել հետևյալ կերպ.
    ~~~C#
    GetComponent<PlayerInput>().SwitchCurrentActionMap("UI");
    ~~~
Իսկ եթե օգտագործում ենք Asset-ի կլասսը, ապա ինփութը հասկանալու համար կամ ստուգում ենք, թե որ մապիցա եկել, կամ էլ մապերը Disable կամ Enable ենք անում
* **Behavior** - Վարքագիծը, կա 4 տարբերակ
    * **Send Messages** - Օգտագործումա յունիթիի ստանդարտ մեսիջ ուղարկելու սիստեմը, այն կկանչի հինթում նշված ֆունկցիաները յուրաքանչյուր սքրիփթում, որը կկցվաշ կլինի այդ գեյմաբջեքթին
    * **Brodcast Message** - Վերևինի նմանա, այն բացառությամբ, որ սրանով մեսիջները կանչվում են նաև դաչեռնի գեյմաբջեքթներում
    * **Invoke Unity Events** - Օգտագործումա յունիթիի ստանդարտ ինվոկի մեխանիզմը, այսինքն ֆունկցիան մենք ենք տալիս, ու բացի մեյն ֆունկցիայից, կարող ենք տալ նաև հետևյալ էվընթները
        * **Device Lost Event** - Երբ օրինակ մկնիկն անջտվեց
        * **Device Regained Event** - Երբ մկնիկը նորից վերականգնվեց
        * **Controls Changed Event** - Անցում օրինակ կիբորդից գեյմփադի
        > Կարա լինի երբ բաթընը մի անգամ ենք սեղմում, բայց Invoke-ի ֆունկցիան 3 անգամա կանչվում, էտ նրանիցա, որ չենք տվել սեղմելու կոնկրետ իվենթն, ու ինքը կանչումա **Start**(KeyDown), **Performed**(KeyHold) ու **Canaceled**(KeyUp) իվընթները, կանչված իվենթը կարանք ստուգենք հետևյալ կերպ․
        ~~~c#
        using UnityEngine.InputSystem
        ...
        public void MyFunc(InputAction.CallbackContext context)
        {
            Debug.Log(context.phase)
            if(Contect.performed) {...} // երբ սեղմածա
        }
        ~~~
    * **Invoke C Sharp Event** - Ֆունկցիան/երը սահմանում ենք սքրիփթում, օգտագործոլով կամպանենտի ֆիչերը
        ~~~c#
        private PlayerInput playerInput;
        
        private void Awake(){
            playerInput = GetComponent<PlayerInput>();
            PlayerInput.onActionTriggered += PlayerInput_onActionTriggered;

            // Ավելացնումա իվենթ, հասանելի են "+=" և "-=" գործողությունները
            // onActionTrigger-ի փոխարեն(զուգահեռ) կարող ենք տալ ստանդարտ Lost, Regained, Changed իվենթները
            // "+=" գրելուց հետո հինթում կառաջարկի PlayerInput_onActionTriggered քիվորդը, tab-ը սեղմելով կգրվի ու տակից կավելացվի իվենթը, որի անունը հետո արդեն կարանք փոխենք ու ներսում գրենք մեր ուզածը (ներսի եղածը կարանք ջնջենք)
            playerInput.onActionTriggered += PlayerInput_onActionTriggered;
        } 
        // Ֆունկցիան որպես արգումենտ ստանումա CallbackContext, որը մեզ հնարավոությունա տալիս կառավարել իվենթը
        private void PlayerInput_onActionTriggered(InputAction.CallbackContext context)
        {
            // Կտպի, որ Action Map-ի որ Action-ի որ Event-ն  կանչվել, phase-ն և ժամը
            Debug.Log(context);
        }
        ~~~



## C# Class
Երբ "Input Action Asset"-ի վրա սեղմենք, ինսպեքթրում կառաջարկի գեներացնել c# class: Գեներացնելով այն, տվյալ Input Action Asset-ի իվենթներին կարող ենք դիմել ցանկացած այլ սքրիփթներից՝ ստեղծելով այդ կլասսի փոփոխական, օր՝
~~~C#
MyClass obj = new MyClass();
obj.MapName.ActionName.performed += Jump_performed;

private void Jump_Performed(InputAction.CallbackContext context)
{
    ...
}
~~~
Այս դեպքւմ "Player Input Component"-ի անհրաժեշտություն այլևս չկա

Վարոնշյալ կոդը սակայն չի աշխատի, քանի որ լիթները միացված չի, այն կարելի է միացնել մի քանի ձևերով, օր՝
~~~C#
MyClass obj = new MyClass();
obj.Enable(); // կմիացնի սակայն բոլոր մափերի էքշնները
obj.MapName.Enable(); // կմիացնի այդ մափը միայն
~~~


## Script Examples

~~~C#
if(Mouse.current.leftButton.wasPressedThisFrame) {...} //ոչ Input System-ի կլասսա պետք, ոչ էլ ասսեթ
~~~

~~~C#
[...]
bool wasInteractionPressed = false;
[...]
controls.GamePlay.Interact.performed += ctx => wasInteractionPressed = true; // եթե համապատասխան էքշընը սկսվելա
controls.GamePlay.Interact.cancelled += ctx => wasInteractionPressed = false; // եթե ավարտվելա
[...]
~~~

## UI
* **Create UI Image > AddComponent[On-Screen Stick] > Control Path > Gamepad > Left Stick** - Նկարին կտա գեյմփադի ստիկի պարամետրերը
* **Create UI Image > AddComponent[On-Screen Button] ... > նկարին կտա ընտրված բաթնի ֆունկցիոնալը