
//hola

/**
 * esto es un comentario de varias lineas
 */
let num: number = 1;
let str: string = "string";
let b: boolean = true;

if(b){
    printline("this");
}

while (num < 3){
    if(num==2){
        printline("if inside while");
        readline();
    }
    printline(num);
}

const message: string = "hello world";
printline(message);