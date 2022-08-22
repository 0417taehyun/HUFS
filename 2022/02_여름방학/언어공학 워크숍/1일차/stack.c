// C의 배열(Array)을 활용한 스택(Stack) 구현

#include <stdio.h>
#define STACK_SIZE 3

typedef int element;
element stack[STACK_SIZE];
int top = -1;

void push(element item) {
    if (top == STACK_SIZE - 1) {
        printf("\nStack is full!\n");
        return;
    } else {
        stack[++top] = item;
    }
}

element pop() {
    if (top == -1) {
        printf("\nStack is empty!\n");
        return 0;
    } else {
        return stack[top--];
    }
}

element peek() {
    if (top == -1) {
        printf("\nStack is empty!\n");
        return 0;
    } else {
        return stack[top];
    }
}

void del() {
    if (top == -1) {
        printf("\nStack is empty!\n");
    } else {
        top--;
    }
}

void printStack() {
    int i;
    printf("\nSTACK [ ");
    for (i = 0; i <= top; i++) {
        printf("%d ", stack[i]);
    }
    printf("]\n");
}


void main() {
    // 아직 스택에 아무런 값도 입력하지 않았기 때문에 쓰레기 값을 반환한다.
    printf("Before push: %d\n", stack[2]);

    printf("Current Top Index: %d\n", top);

    int value;
    for (value = 1; value <= 4; value++) {
        push(value);
        printStack();
        printf("Current Top Index: %d\n", top);
    }

    int item;
    item = peek();
    printf("\nCurrent Top Item: %d\n", item);

    del();
    printStack();
    printf("Current Top Index: %d\n", top);

    // 현재 가리키는 최상단의 인덱스만 del() 함수를 통해 수정한 것이기 때문에 기존에 저장되어있던 값은 여전히 남아있다.
    printf("Before delete value: %d\n", stack[2]);

    // 물론 아래와 같이 배열의 요소는 덮어쓸 수 있다.
    stack[2] = 10;
    printf("Before delete value: %d\n", stack[2]);

    /* 정해진 크기를 초과한 요소를 출력하는 경우 배열에 할당된 영역을 벗어난 메모리를 사용한다.
     * 이 경우 포인터 연산을 통해 접근하기 때문에 컴파일러가 에러 메시지가 아닌 경고 메세지를 띄운다.
     * 범위를 벗어난 영역에 접근하는 배열 코드는 실제 실행 단계에서나 문제를 일으키기 때문에 추후 디버깅에 어려움이 있다.
     * 따라서 사용 범위를 초과해서 사용하지 않게 하기 위해 유의해야 한다.
     */
    printf("Over the size: %d\n", stack[9999]);

    int _;
    for (_ = 0; _ <= 2; _++) {
        item = pop();
        printStack();
        printf("Current Top Item: %d\n", item);
    }
}