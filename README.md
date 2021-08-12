## 📝 Table of Contents
- [그리디](#그리디)
- [구현](#구현)
- [DFS/BFS](#DFS/BFS)
- [정렬](#정렬)
- [이진탐색](#이진탐색)
- [동적계획법](#동적계획법)
- [최단 경로](#최단-경로)
- [그래프 탐색](#그래프-탐색)

---
### 그리디

|번호|        추천 문제      |                               문제 번호                                  |                                          문제 이름                                 |                                       난이도                                     | 문제풀기 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14916" target="_blank">14916</a> | <a href="https://www.acmicpc.net/problem/14916" target="_blank">거스름돈</a>      | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |   ✅   |      
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1343" target="_blank">1343</a>   | <a href="https://www.acmicpc.net/problem/1343" target="_blank">폴리오미노</a>     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |   ✅   |      
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2217" target="_blank">2217</a>   | <a href="https://www.acmicpc.net/problem/2217" target="_blank">로프</a>           | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |   ✅   |      
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/13305" target="_blank">13305</a> | <a href="https://www.acmicpc.net/problem/13305" target="_blank">주유소</a>        | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |   ✅   |      
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1758" target="_blank">1758</a>   | <a href="https://www.acmicpc.net/problem/1758" target="_blank">알바생 강호</a>    | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |   ✅   |      
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20300" target="_blank">20300</a> | <a href="https://www.acmicpc.net/problem/20300" target="_blank">서강근육맨</a>    | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> |   ✅   |      
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11399" target="_blank">11399</a> | <a href="https://www.acmicpc.net/problem/11399" target="_blank">ATM</a>           | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |   ✅   |      
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11508" target="_blank">11508</a> | <a href="https://www.acmicpc.net/problem/11508" target="_blank">2+1 세일</a>      | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |   ✅   |      
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20115" target="_blank">20115</a> | <a href="https://www.acmicpc.net/problem/20115" target="_blank">에너지 드링크</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |   ✅   |      
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1931" target="_blank">1931</a>   | <a href="https://www.acmicpc.net/problem/1931" target="_blank">회의실 배정</a>    | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |   ✅   |      
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1541" target="_blank">1541</a>   | <a href="https://www.acmicpc.net/problem/1541" target="_blank">잃어버린 괄호</a>  | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |       |      
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20365" target="_blank">20365</a> | <a href="https://www.acmicpc.net/problem/20365" target="_blank">블로그2</a>       | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |   ✅   |      
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11047" target="_blank">11047</a> | <a href="https://www.acmicpc.net/problem/11047" target="_blank">동전 0</a>        | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |       |      
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21758" target="_blank">21758</a> | <a href="https://www.acmicpc.net/problem/21758" target="_blank">꿀 따기</a>       | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/>        |      
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16953" target="_blank">16953</a> | <a href="https://www.acmicpc.net/problem/16953" target="_blank">A → B</a>         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |       |      
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21314" target="_blank">21314</a> | <a href="https://www.acmicpc.net/problem/21314" target="_blank">민겸 수</a>       | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |       |      
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11000" target="_blank">11000</a> | <a href="https://www.acmicpc.net/problem/11000" target="_blank">강의실 배정</a>   | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/13164" target="_blank">13164</a> | <a href="https://www.acmicpc.net/problem/13164" target="_blank">행복 유치원</a>   | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 19 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2141" target="_blank">2141</a>   | <a href="https://www.acmicpc.net/problem/2141" target="_blank">우체국</a>         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 20 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/19598" target="_blank">19598</a> | <a href="https://www.acmicpc.net/problem/19598" target="_blank">최소 회의실 개수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 21 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2812" target="_blank">2812</a>   | <a href="https://www.acmicpc.net/problem/2812" target="_blank">크게 만들기</a>       | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 22 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2212" target="_blank">2212</a>   | <a href="https://www.acmicpc.net/problem/2212" target="_blank">센서</a>              | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 23 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1092" target="_blank">1092</a>   | <a href="https://www.acmicpc.net/problem/1092" target="_blank">배</a>                | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 24 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/13975" target="_blank">13975</a> | <a href="https://www.acmicpc.net/problem/13975" target="_blank">파일 합치기 3</a>    | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |       |      
| 25 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1715" target="_blank">1715</a>   | <a href="https://www.acmicpc.net/problem/1715" target="_blank">카드 정렬하기</a>     | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |       |      
| 26 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2285" target="_blank">2285</a>   | <a href="https://www.acmicpc.net/problem/2285" target="_blank">우체국</a>            | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |       |      
| 27 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/8980" target="_blank">8980</a>   | <a href="https://www.acmicpc.net/problem/8980" target="_blank">택배</a>              | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |       |      

---
### 구현

---
### DFS/BFS

---
### 정렬

---
### 이진탐색

---
### 동적계획법

---
### 최단 경로

---
### 그래프 탐색
