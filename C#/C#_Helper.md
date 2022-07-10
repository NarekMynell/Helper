* .Net Freamwork-ը ծրագրավորման փաթեթա C#-ի, F#-ի, Visual Basic-ի համար
    * CLR (Common Language Runtime), օրինակ՝ հոսքերի կառավարում, գերբիջ քլեքոըր ...
    * .Net Freamwork Class Library
* .Net Freamwork-ը միանգամից բինար կոդի չի թարգմանում, այլ՝ CIL-ի (Common Intermediate Language)
* C#-ում նույնպես կարող ենք օգտագործոլ ցուցիչներ, սկայն դա ապահով չի ու CLR-ից դուրսա (դա անելու համար պետքա ստեղծել unsafe քիվորդով բլոկ, որի տակ եղածի համար CLR-ը պատասխանատու չի)
* Alias-ներով օրինակ կարում ենք using արած փեքիջների անունը փոխենք, որ եթե մի անունով ֆունկցիան տարբեր լիբերում կա ...
* Թվի մեջ կարող ենք անդրսքորեր դնել ընթերնելիության համար (օր՝ int a = 1_000_000;)
* /// դնելով ֆունկցիայի վր կարող ենք summary(hint) գրել
* **??** Օպերատոր
    ~~~C#
    Console.WriteLine(a ?? b); // Եթե a-ն նալա կտա b-ն
    (n ??= new List<int>()).Add(5); // Եթե n-ը նալա, ապա կկատարի վերագրում
    ~~~
* **? (Nullable value types)**
    ~~~C#
    double? x = null; // Ստանդարտ տիպերի արժեքների բազմությանն ավելացնումա null-ը
    ~~~
* **Boxing/Unboxing** - Boxing-ն այն պրոցեսնա, երբ վալյու թայփը վերածում ենք ռեֆերենս թայփի։ Սա ստեղծվելա, երբ դեռ չկաին ջեներիքներն ու պոլիմորֆիզմի կարիք կար։ Օրինակ քանի որ ռեֆերենս ու վելյու թայփերն ընդհանուր նախնի չունեին, ֆունկցիայի արգումետի տիպը չէինք կարա տաինք նենց բան, որ 2 ձևերն էլ ընդուներ։ Դրա համար օրինակ int-ը վերածում էինք object-ի ու նոր փոխանցում ֆունկցիային։
* [Extensions](https://www.geeksforgeeks.org/extension-method-in-c-sharp/#:~:text=In%20C%23%2C%20the%20extension%20method,re%2Dcompile%20the%20original%20type.)-ի միջոցով

## String
* **StingBuilder** կլասսը օպտիմալ տարբերակա, երբ անհրաժեշտա սթրինգը մաս-մաս հավաքել
* " նշանը սթրինգում պահելու համար պետքա "" գրել (իհարկե տողից առաջ ունենալով @)
~~~C#
string s0 = $"{a} + {b} = {c}"; // Պարզա
string s1 = @"line \r\n new line"; // Քիվորդերը կարդումա որպես սովորական տեքստ
~~~

## Functions Expressions
* **Delegate** - C++ -ի ցուցիչների նմանա, որոնց կարելիա ֆունկցիաների ռեֆերենսներ վերագրել, լինում են Action և Func տիպերի, որոնցից ամեն մեկն էլ ունի իրա առանձին գրելաձևը, սակայն հենց Delegate-ն կարա երկուսի գործն էլ անի
    ~~~C#
    [modifiers] delegate [return type] Name ({parameters})
    ~~~
    Դելեգատները լինում են **Singlecast** (Վերագրվում են մեկ ֆունկցիայի) և **Multicast** (Վերագրվում են մեկից ավելի ֆունկցիաների, իսկ կանչելուց բոլորը կանչվում են)
    Դելեգատներին կարելի է վերագրել անանուն ֆունկցիաներ․
    ~~~C#
    public delegate void NoParam();

    static void Main()
    {
        NoParam noPrm = delegate ()
        {
            Console.WriteLine($"bla bla");
        }

        noPrm();
    }
    ~~~

    Դելեգատները շատ հարմարա կոկիկ ու օպտիմիզացված կոդ գրելու համար, օրինակ՝ [վիդեոյի վերւին մասը](https://www.youtube.com/watch?v=3ZfwqWl-YI0)

* **Lambda Function** - Դելեգատներին կարելի է վերագրել Lambda Function.
    ~~~C#
    public delegate void TestDelegate();
    private TestDelegate testDelegateFunction;

    void Start()
    {
        testDelegateFunction += () => { Debg.Log("First"); };
        testDelegateFunction += () => Debug.Log("Second");
    }
    ~~~

    Labda-ների վատը նայա, որ օրինակ վերևի դելեգատից չենք կարող ջնջել հենց առաջին ֆունկցիան

* **Action** (Action Delegate) - Դելեգատների նմանա, այն տարբերությամբ, որ արժեք չի վերադարձնում
* **Func** (Function Delegate) - Ստանում և վերադարձնումա

## VS

* **Ctrl + Tab** - Թաբերի վրայով արագ ցատկեր
* **Ctrl + Shift + Space** - Երբ ֆունկցիայի փակագիծը բացում ենք ու այն ունենումա վերբեռնումներ, ափա սլաքների կնոկեքը սեղմելով անցումներ ենք կատարում
* **Ctrl + K + Crtl + D** - Եթե կոդը խառնվածա, դզումա
    * Ctrl + K + D(F) - Սելեքթ արած տեքստի համար միայն
* **Ctrl + U** - Փոքրատառա սարքում
    * Shift + Ctrl + U - Մեծատառա սարքում







## Interfaces

* **IComparable** - Համեմատության սահմանումը
    ~~~C#
    public class Node<T> where T : IComparable
    {
        ...
        public int CompareTo(object obj)
        {
            if (obj == null) return 1;

            Node<T> otherTemperature = obj as Node<T>;
            if (otherTemperature != null)
                return this.Value.CompareTo(otherTemperature.Value);
            else
                throw new ArgumentException("Object is not a Temperature");
        }
    }
    ~~~

* **IEmumerable** - Իտեռացիաների սահմանումը
    ~~~C#
    public class BST<T> : IEnumerable<Node<T>> where T : IComparable
    {
        ...
        public IEnumerator<Node<T>> GetEnumerator()
        {
            if (Root.Left != null)
                foreach (Node<T> node in LeftTree)
                    yield return node;

            yield return Root;

            if (Root.Right != null)
                foreach (Node<T> node in RightTree)
                    yield return node;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            throw new NotImplementedException();
        }
    }
    ~~~




## Threading
* **ThreadStart** - Հատուկ դելեգատա, որը կարող ենք տալ նոր թրեդին։ Կարանք էտ դելեգատի օբյեկտ սարքենք,հիմական ֆունկցիան աելացնենք հետո էլ քոլբեք ֆունկցիա ու տանք թրեդին, որը հերթականությամբ կկանրի սբսքրաբերներին։ <ins>Սակայն քալբաքը կկանչվի էլի էտ թրեդում, ոչ թե մեյնում։</ins>
* **Եթե հարկավորա թրեդի ավարտի մասին քոլբեք ստանալ մեյն թրեդում։** [Ավելի մանրամասն](https://metanit.com/sharp/tutorial/13.3.php)
    ~~~C#
    async void MyFunc()
    {
        await Task.Run(() => { /* your work in thread */ });
        //Your work is finished at this point
    }
    ~~~



## LINQ
* dfdfd
    ~~~C#
    // Specify the data source.
    int[] scores = { 97, 92, 81, 60 };

    // Define the query expression.
    IEnumerable<int> scoreQuery =
        from score in scores
        where score > 80
        select score;

    // Execute the query.
    foreach (int i in scoreQuery)
    {
        Console.Write(i + " ");
    }

    // Output: 97 92 81
    ~~~

* Կստեղծի list չկրկնվող պատահական թվերով
    ~~~C#
    List<int> list = System.Linq.Enumerable.Range(0, 10).ToList();
    System.Random rnd = new();
    list = list.OrderBy(item => rnd.Next()).ToList();
    ~~~