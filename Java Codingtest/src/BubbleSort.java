/*
 * Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */

import java.util.ArrayList;
import java.util.Arrays;

public class BubbleSort {

    public static int[] bubbleSort(int[] arr) {

        for (int i = arr.length ; i > 0 ; i--){
            for (int j = 1; j < i ; j++)
            {
                if (arr[j] < arr[j-1])
                {
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                }
            }
        }

        return arr;
    }
    public static void main(String[] args) {
        /* 버블 정렬의 특징
        - 시간 복잡도 : 거의 모든 경우에서 O(n^2)으로 성능이 매우 나쁘다.
        - 제자리 정렬이다.
        - Stable sort이다.
         */
        int[] arr = {6,3,10,-3,-10,0,17};
        int[] result = bubbleSort(arr);
        for (int i = 0; i < result.length ; i ++) System.out.println(result[i]);
    }
}
