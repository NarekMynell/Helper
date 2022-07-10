## Directives
* **#pragma kernel FunctionKernel** - kernel-ը main ֆունկցիայի քիվորդնա։ Որպես մեյն ֆունկցիա տալիս ենք մեր գրած FunctionKernel-ը

## Types

* **bool** - true or false
* **int** - 32-bit signed integer
* **half** - 16-bit floating point value
* **float** - 32-bit floating point value
* **double** - 64-bit floating point value
<br>
* **vector <type, size>** or **typeN** - type տիպի size չափսի վեկտոր, օր՝
    ~~~
    vector <float, 4> Vector;
    float4  Vector;
    float  Vector[4];
    ~~~

* **matrix<type, M,N>** or **typeMxN** - type տիպի M x N չափսի մատրից, օր՝
    ~~~
    #pragma pack_matrix (row_major); // ընտրում ենք մատրիցների օրենտացիան
    float4  Vector;
    float  Vector[4];
    ~~~

* **if (expr) then statement [else statement]**
<br>
* **do statement while (expr);**
* **while (expr) statement;**
* **for (expr1;expr2;expr3) statement**

## Functions

* **ceil(x)** - Վերադարձնումա x-ից մեծ կամ հավասար ամենափոքր ամբողջ թիվը
* **floor(x)** - վերադարձնումա x-ին հավասար կամ փոքր ամենամեծ ամբողջ թիվը
* **distance(a, b)** - Վերադարձնումա հեռավորությունը
* **len(v)** - Վերադարձնումա վեկտորի չափսը
* **lenght(v)** - Վերադարձնումա վեկտորի երկարությունը
* **normalize(v)** - Վերադարձնումա նորմալիզացված վեկտորը