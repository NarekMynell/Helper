# Unity
## Basics
* **Component[] GetComponentsInChildren(Type t, bool includeInactive);** - Ստանումա կոմպոնոնտները բոլոր չիլդերից


## Mathf

* **Clamp01**
    ~~~
    // Վերադարձնումա 0-1 դիապազոնի թիվ
    float Clamp01(float value)
    ~~~
* **Lerp**
    ~~~
    // Գնումա a-ից b
    // t-ն ինքնա իրա մեջ Clamp01 անում
    float Lerp(float a, float b, float t)
    ~~~
* **LerpUnclamped**
    ~~~
    // Գնումա a-ից b առանց t-ի որևէ clamp-ի
    // Արդյունքը կարա դուրս գա [a, b] դիապազոնից
    float LerpUnclamped(float a, float b, float t)
    ~~~
* **SmoothStep**
    ~~~
    // Գնումա from-ից to աստիճանաբար դանդաղելով
    // t-ն ինքնա իրա մեջ Clamp01 անում
    float SmoothStep(float from, float to, float t)
    ~~~
* **CeilToInt**
    ~~~
    // Վերադարձնումա f-ից մեծ կամ հավասար ամենափոքր ամբողջ թիվը
    int CeilToInt(float f)
    ~~~
* **Repeat**
    ~~~
    // t-ն վերադարձնումա [0, lenght] դիապազոնում
    float Repeat(float t, float length);
    ~~~


## Transform
* **[Transform.Translate(Vector3 translation, Space relativeTo = Space.Self)](https://docs.unity3d.com/ScriptReference/Transform.Translate.html)** - Տեղափոխումա օբյեկտը translation ուղղությամբ և չափով 1 unit/վ արագությամբ
* ```obj.transform.forward;``` - Կտա կապույտ առանցքի նորմալայզիդ փըզիշընը
* ```transform.LookAt(target);``` - Forward առանցքը կպտտի target վեկտորի ուղղությամբ
* ```Quaternion.LookRotation(Vector3 forward, Vector3 upwards = Vector3.up);``` - կվերադարձնի Quaternion պտտված forward-ի ուղղությամբ
* ```transform.rotation = Quaternion.Slerp (transform.rotation, Quaternion.LookRotation (desiredMoveDirection), desiredRotationSpeed);``` - Slerp-ի օրինակ, Slerp-ը Lerp-ի նման է, պարզապես պտույտների համար

## Input
* **[Input.GetAxis(string axisName)](https://docs.unity3d.com/ScriptReference/Input.GetAxis.html)** - Վերադարձնումա մկնիկի կամ ժյոստիկի տվյալ առանցքի նկատմամբ սեղմվածության չափը
~~~C#
    myV3 = myTransform.TransformDirection(myv3); // myTransform-ի լոկալ վեցտորը դարձնումա գլոբալ
~~~

* ```OnMouseDown()``` - Կկանչվի, երբ քլիք լինի GUI էլեմենտի կամ քլայդերի վրա։
* ```RectTransformUtility.ScreenPointToLocalPointInRectangle(...)``` - Կստուգի արդյոք տրված պզիշընը գտնվումա տրված RectTransform-ի մեջ։ Եթե այո՝ կտա նաև լոկալ պզիշընը։
* ```EventSystem.current.IsPointerOverGameObject()``` - Ստուգումա արդյոք UI-ի վրայա պօինթերը
  ~~~c#
    // 
    private void Update()
    {
        if (input.Player.GetPointer.WasPressedThisFrame() && !EventSystem.current.IsPointerOverGameObject(input.Player.PointerId.ReadValue<int>())) ...
    }
  ~~~
* [PointerDownEvent](https://docs.unity3d.com/ScriptReference/UIElements.PointerDownEvent.html) - Քլասա, երբ պօինդերը սեղմվումա։ Մալթիթաչի դեպքում առաջին թաչնա միայն հենդլ անում


## Editor
* [OnDrawGizmos](https://docs.unity3d.com/ScriptReference/MonoBehaviour.OnDrawGizmos.html) - Սցենայում պատկերումա ուղղանկյունանիստ
* [Custom Editors](https://docs.unity3d.com/Manual/editor-CustomEditors.html) - Հնարավորությունա տալիս քասթըմ քամփանենթների համար քասթըմ ինսպեկտըր սարքել



## Attributes
* ```[space]``` - տարածեւթյունա տալիս
* ```[Header("MyHeader")]``` - Վերնագիրա տալիս
* ```[SerializeField, Range(1, 10)]``` - Slider-ովա ստեղծում
* ```[Tooltip("Hint Text")]``` - Դեսքրիփշնա տալիս հինթի տեսքով
* ```[HiddenInInspector]``` - Նենցա անում, որ ինսպեկտրում չերևա
* ```[ColorUsage(bool, bool, bool)]``` - Տալիս ենք Color տիպի օբյեկտին, որպեսզի սահմանենք ինսպեկտրում պոլիտրայի ձևը
* ```[ExecuteAlways]``` - Սքրիփթը միշտ կատարվումա, նաև սցենայում
* ```[HelpURL(InputSystem.kDocUrl + "/manual/OnScreen.html#on-screen-sticks")]```
* ```[RuntimeInitializeOnLoadMethod]``` - Հնարավորությունա տալիս ոչ MonoBehawiour կլասսի ֆունկցիային կատարվել


* **[Menu Item](https://docs.unity3d.com/ScriptReference/MenuItem.html)** - Հնարավորությունա տալիս ինտերֆեյսում մենյուներ և/կամ դրանց կետեր ավելացնել ու սահմանել գործողություն, ինչպես նաև shortcut-եր սահմանել
Ֆունկցիաները հնարավոր է սահմանել ցանկացած սքրիփթում
* **[Context Menu](https://docs.unity3d.com/ScriptReference/ContextMenu.html)** - Հնարավորությունա տալիս կոնտեկստ մենյոււմ (կամպանենտի kebab մենյունա) ավելացնել նոր բաժին
* **[Asset Menu Attribute](https://docs.unity3d.com/ScriptReference/CreateAssetMenuAttribute.html)** - Ստեղծումա Assets/Create մենյուում նոր ատրիբուտ։ [Տես](https://answers.unity.com/questions/1146958/createassetmenuattribute-menuname-and-order-constr.html)
* **[Execute In Edit Mode](https://docs.unity3d.com/ScriptReference/ExecuteInEditMode.html)** - Հնարավորությունա տալիս սքրիփթներին աշխատել էդիդ մոդում
* **[Require Component](https://docs.unity3d.com/ScriptReference/RequireComponent.html)** - Ստիպումա, որպեսզի օբյեկտը պարտադիր ունենա նշված կամպանենտը
* **[Add Component Menu](https://docs.unity3d.com/ScriptReference/AddComponentMenu.html)** - Հնարավորությունա տալիս կոմպոնենտներ ստեղծել
* **[Custom Property Drawer](https://docs.unity3d.com/ScriptReference/PropertyDrawer.html)** - Հնարավորույունա տալիս քասթըմ ատրիբուտներ գրել

## Asynchronous programming
* **Invoke** - Corutines-ի նման բանա, սակայն ավելի պարզ մեխանիզմա, ի տարբերոթյուն կորուտինների, էստեղ պաուզաներ կամ պաուզաների փոփոխություններ չենք կարա տանք
    ~~~c#
        void Start{
            Invoke("MyFunc", 1); //կկանչի ֆունկցիան 1 վայրյան հետո
            Invoke("MyFunc", 1, 2); //կկանչի ֆունկցիան 1 վայրյան հետո, այնուհետև ամեն 2 վայրկյանը մեկ
        }
    ~~~

## Events
* ```OnGUI``` - Ֆունկցիան լայֆսայքլի ֆունկցիայա, որը կարա մի կարդրի ժամանակ մի քանի անգամա կանչվի։ Այն իրականացնում է UI-ի ռենդերինգը
    ~~~C#
        private void OnGUI()
        {
            Event ev = Event.current;
            if (ev.keyCode == KeyCode.A)
                Debug.Log("Pressed A ");
        }
    ~~~
* ```IPointerDownHandler, IPointerUpHandler, IDragHandler``` ինտերֆeյսներ
Այս ինտերֆեյսներն ունեն ամեն մեկը մեկական քոլբեքի ֆունկցիաներ՝ համանուն իվենթների որոշման համար։ Պետքա սքրիպթը կցել գեյմօբյեկտին և իմպլեմենտացնել այս ինտերֆեյսները, ու դրանք հենդլ կանեն կցված օբյեկտին քլիք անելու իվենթները։
    * Սովորական օբյեկտների համր պետքա կամեռային միացված լինի ՝՝՝Physics Raycaster՝՝՝
    * UI էլեմենտների համար պետքա քանվասին միացված լինի ```Graphic Raycaster```
    * Պետքա սցենայում լինի "EventSystem" օբյեկտ՝ ```Event System``` և ```Input System UI Iput Module``` կամպանենտներով

## UI
* UI-ն Unity-ում ունի 3 տարբերակ
    * **UI Toolkit** - Նոր ստանդարտ
    * **Unity UI** - Սովորականը
    * **IMGUI** - Օգտագործումա էդիթըրի համար
        ~~~C#
        // Կստեղծի բոքս տրված անունով
        GUI.Box(new Rect(10, 10, 100, 90), "Loader Menu");

        // Բոլոր կոմպոնենտների բեք գույների սահմանաում
        GUI.backgroundColor = Color.green;

        // Միանգամից կստեղծի ու հենդլ կանի
        if(GUI.Button(new Rect(50, 50, 100, 25), "My Button")) do something

        // Ստեղծում է սթայլ, որը կարող ենք տանք օրինակ բաթընին
        GUIStyle style = new GUIStyle(GUI.skin.box);
        style.normal.textColor = Color.blue;
        style.fontSize = 38;

        // Կստեղծի տեքստային դաշտ style սթայլով
        GUI.Label(new Rect(10, 0, 0, 0), "Rotating on X:" + x + " Y:" + y + " Z:" + z, style);
        ~~~
* **Cursor**
    ~~~C#
    // Բերումա սովորական ռեժիմի և էկրանի կենտրոն
    Cursor.lockState = CursorLockMode.None;
    // Հայդա անում կուրսորն ու պահում էկրանի մեջ
    Cursor.lockState = CursorLockMode.Locked;
    // Չի թողնում, որպեսզի կուրսորը դուրս գա խաղի էկրանի տարածքից
    Cursor.lockState = CursorLockMode.Confined;
    ~~~
* **RectTransform**
    ~~~C#
    // Արդյոք պզիշընը գտնվեւմա ռեքթթրանսֆորմի մեջ
    bool RectangleContainsScreenPoint(RectTransform rect, Vector2 screenPoint, Camera cam);
    ~~~
* **Graphic Raycast**
    ~~~C#
    // Կտա UI էլեմենտի անունը, եթե  myPos-ում այն գոյություն ունի
    PointerEventData eventData = new PointerEventData(EventSystem.current);
    eventData.position = myPos;
    List<RaycastResult> raysastResults = new List<RaycastResult>();
    EventSystem.current.RaycastAll(eventData, raysastResults);
    if (raysastResults.Count > 0)
        Debug.Log(raysastResults[0].gameObject.name);
    ~~~



## Components
* **Renderer** - Սրա միջոցով հնարավորա հասանելիություն ստանալ մատերիալին, մեշին, ստվերներին և այլն, օր՝
    ~~~C#
        Renderer[] characterMaterials;
        void Start(){
            characterMaterials = GetComponentsInChildren<Renderer>(); //Ստանումա ցիլդերի բոլոր րենդերեր հանդիսացող կամպանենտները
        }
        void MyFunc(){
            for (int i = 0; i < characterMaterials.Length; i++){
                if (characterMaterials[i].transform.CompareTag("PlayerEyes"))
                    characterMaterials[i].material.SetColor("_EmissionColor", eyeColors[i])
            }
        }
    ~~~

* **Character Controller** - սա կցում ենք մեր փլեյերին, որը ռիդիջբդի պիտի չունենա, սա տալիս է ռիդիջբդիի հատկություններ և քափսուլ-քլայդեր
    ~~~C#
        GetComponent<CharacterController>().Move(moveDir); // կտեղափոխի moveDir ուղղությամբ կապույտ ռանցքի նկատմամբ
    ~~~



## Ray

~~~C#
    Ray ray = new Ray(startPos, dir); // կստեղծի ճառագայթ startPos սկզբով և dir ուղղությամբ
    Debug.DrawRay(startPos, dir, Color.red, 1f); // էդիթևրում կպատկերի ճառագայթը
    Physics.Rayast(ray); // կտա true, եթե ճառագայթն կպել է ինչ-որ քլայդերի

    RaycastHit hit; // Փոփոխականն օգտագործվում է ճառագայթի քլիշընի մասին ինֆո ստանալու համար
    if(Physics.Raycast(ray, out hit)) // եթե դիպչելա։ hit-ում գտնվումա ինֆորմացիան դիպչման մասին
        { Debug.Log("charagaytn dipchela inch-vor collideri") }

    Physics.Raycast(cam.ScreenPointToRay(Input.mousePosition), out hit) // քլիքի ուղղությամբ կամեռայից ճառագայթ

    int triangleIndex = hit.triangleIndex; // կտա եռանկյան առաջին վերտեքսի ինդեքսը
~~~



## Mesh
~~~C#
    Mesh mesh = meshCollider.sharedMesh;
    Vector3[] normals = mesh.normals; // վերտեքսների նորմալները
    Vector3[] vertecies = mesh.vertices;
    int[] triangles = mesh.triangles; // կտա եռանկյունների վերտեքսների ինդեքսները  mesh.vertices-ում 
    mesh.uv = new Vector2[] { new Vector2(0, 0), new Vector2(0, 1), new Vector2(1, 1) }; // 3 վեռտեքսանի մեշի համար ստեղծումա uv քարտեզ
~~~
~~~C#
myMesh.MarkDynamic(); // Մեշը օպտիմիզացնումա հաճախակի փոփոխությունների համար
~~~



## Material
* **MaterialPropertyBlock** - Հնարավորությունա տալիս փոփոխել մատերիալի փրոփրթիները տարբեր օբյեկտների համար առանց նոր մատերիալ սարքելու

## Textures
* ```mySprite = Sprite.Create(texture, new Rect(0, 0, texture.width, texture.height), Vector2.zero);``` - տեքստուրան կդարձնի սպրայթ


## Physic
* Rigidbody օբյեկտները շարժման ընթացքում հասնելով փոքր արագության կանգնում են ու ֆիզիկայի աբդեյթը դադարումա, մինչև իրենց վրա նորից ֆիզիկա չի ազդի։ Սա արվումա օպտիմիզացիայի նպատակով, և եթե դադարից հետո սքրիփթից թրանսորմով ուզենանաք շարժենք, օբյեկտի ֆիզիկան կարա չմիանա։ Այն միացնելու համար հարկաորա կանչել **WakeUp** ֆունկցիան։
* **Colliderner**-ի հպումներ
    * OnCollisionEnter
    * OnCollisionStay
    * OnCollisionExit
* **Trigger**-ների հպումներ
    * OnTriggerEnter
    * OnTriggerStay
    * OnTriggerExit
* **AddTorque** - RigidBody-ին կտա պտույտ
* **Rigidbody.position** (Rigidbody.MovePosition)
    ~~~C#
    // RB քըմփոնենթ ունեցող օբյեկտի փզիշնի փոփոխությունն այս մեթոդով ավելի արագա կատարվում
    GetComponent<Rigidbody>().position = Vector3.zero;
    ~~~


## Rendering
* [Application.targetFrameRate](https://docs.unity3d.com/ScriptReference/Application-targetFrameRate.html) - FPS-ը։ Ի տարբերություն vSync-ի սրանով կարողանում ենք ռանթայմ կարգավորել, օրինակ համապատասխան ժամանակ իջացնել խնայողության համար։ Հարմարա մոբայլների համար։ Դիֆոլթով -1-ա (Անջատված)։
* [QualitySettings.vSyncCount](https://docs.unity3d.com/ScriptReference/QualitySettings-vSyncCount.html) - vSync-ն ենք սեթինգ անում ռանթայմ։ Կարա ընդունի 1, 2, 3, 4 արժեքները, որը նշանակումա, թե դիվայսի FPS-ը քանի անգամ պակաս լինի խաղի FPS-ը։ Դիֆոլթով 0-ա (Անջատված)։
* [QualitySettings.maxQueuedFrames](https://docs.unity3d.com/ScriptReference/QualitySettings-maxQueuedFrames.html) - GPU-ում ռենդերինգի ենթակա կադրերի հերթի քանակը։
* [Screen.currentResolution](https://docs.unity3d.com/ScriptReference/Screen-currentResolution.html) - Կտա դիվայս էկրանի չափսերն ու հաճախությունը։




## Unity Collections
* **Unity.Collections** namespace
Այստեղի քլեքշները սկսվում են *Native* անունով և բավարարում են multithreading-ի [Անվտանգության Համակարգին](https://docs.unity3d.com/Manual/JobSystemSafetySystem.html)։ Native-ների վատը նայա, որ նրանք չեն կարող պարունակել Native անդամներ։ Օր՝ չենք կարող գրել ```NativeList<NativeList<T>>```: Native-ներն ունեն իրենց էկվովալենտները Unsafe-ների մեջ։ Իրականում իրենցից ներկայացնում են հենց Unsafe-ներն՝ ավաելցրած անվտանգության մի քանի ֆոկուզներ։
* **Unity.Collections.LowLevel.Unsafe** namespace
Այստեղի քլեքշները սկսվում են *Unsafe* անունով և չեն բավարաում վերոնշյալ անվտանության համակարգին:

> GC-ն չի կառավարում Unity-ի քլեքշները։ Դրանք պետքա կառավարել [ռուչնոյ](https://docs.unity3d.com/Packages/com.unity.collections@1.2/manual/allocation.html)
