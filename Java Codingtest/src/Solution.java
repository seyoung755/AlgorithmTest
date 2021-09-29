/*
 * Copyright (c) 2021. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 * Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
 * Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
 * Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
 * Vestibulum commodo. Ut rhoncus gravida arcu.
 */

import java.util.*;
class Solution {

    private static int N;
    private static boolean[][] visited;
    private static int[][] map;

    private static int[] dx = {-1, 0, 1, 0};
    private static int[] dy = {0, 1, 0, -1};

    private static int cost = Integer.MAX_VALUE;

    public int solution(int[][] board) {
        int answer = 0;
        N = board.length;

        visited = new boolean[N][N];
        map = board;

        // System.out.println(cost);

        BFS(0,0,-1,0);

        answer = cost;

        return answer;
    }


    private static void BFS(int x, int y, int dir, int price) {
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(x, y, dir, price));
        visited[x][y] = true;

        while(!q.isEmpty()) {
            Node node = q.remove();

            int cx = node.x;
            int cy = node.y;
            int cDir = node.dir;
            int cPrice = node.price;

            // 도착
            if (cx == N-1 && cy == N-1) {
                cost = Math.min(cost, cPrice);
            }

            for (int i = 0 ; i < dx.length; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                int nDir = i;
                int nPrice = cPrice;

                // 이동 불가능한 경우
                if (nx < 0 || nx >= N || ny < 0 || ny >= N || map[nx][ny] == 1) {
                    continue;
                }

                // 첫 이동이거나 같은 방향일 때
                if (cDir == -1 || cDir == nDir) {
                    nPrice += 100;
                } else {
                    // 방향이 다를 때
                    nPrice += 600;
                }

                if (!visited[nx][ny] || map[nx][ny] >= nPrice) {
                    visited[nx][ny] = true;
                    map[nx][ny] = nPrice;
                    q.add(new Node(nx, ny, nDir, nPrice));
                    // System.out.println(nPrice);
                }
            }
        }
    }
}

class Node{
    int x;
    int y;
    int price;
    int dir;

    public Node(int x, int y, int dir, int price) {
        this.x = x;
        this.y = y;
        this.price = price;
        this.dir = dir;
    }
}






