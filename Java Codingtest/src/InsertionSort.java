/*
 * Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */

public class InsertionSort {

    public static int[] insertionSort(int[] arr) {

        for (int index = 1 ; index < arr.length ; index++) {
            int temp = arr[index];
            int prev = index - 1;

            while (prev >= 0 && temp < arr[prev]) {
                // temp보다 작으므로 들어갈 자리를 만들기 위해 오른쪽으로 한칸 밀린다.
                arr[prev+1] = arr[prev];
                prev--;

            }
            arr[prev+1] = temp;

        }

        return arr;
    }

    public static void main(String[] args) {
        /* 삽입 정렬의 특징
        - 최선의 경우 O(n)의 시간 복잡도를 가진다. (모두 정렬된 싱태에서 한 요소만 추가되는 경우)
        - 최악의 경우에는 O(n^2)의 시간 복잡도를 가진다.
        - 제자리 정렬이다.
        - Stable sort이다.
         */
        int[] arr = {6,3,10,-3,-10,0,17,-15};
        int[] result = insertionSort(arr);
        for (int i = 0; i < result.length ; i ++) System.out.println(result[i]);
    }
}
