## 📝 Table of Contents
- [그리디](#그리디)
- [구현](#구현)
- [DFS/BFS](#DFS/BFS)
- [정렬](#정렬)
- [이진탐색](#이진탐색)
- [동적계획법1](#동적계획법1)
- [동적계획법2](#동적계획법2)
- [최단 경로](#최단-경로)
- [그래프 탐색](#그래프-탐색)

[백준 문제집](https://github.com/tony9402/baekjoon)


---
### 그리디


|번호|        추천 문제      |                               문제 번호                                  |                                          문제 이름                                 |                                       난이도                                     | 문제 풀기 |
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
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1541" target="_blank">1541</a>   | <a href="https://www.acmicpc.net/problem/1541" target="_blank">잃어버린 괄호</a>  | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |   ✅    |      
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20365" target="_blank">20365</a> | <a href="https://www.acmicpc.net/problem/20365" target="_blank">블로그2</a>       | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |   ✅   |      
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11047" target="_blank">11047</a> | <a href="https://www.acmicpc.net/problem/11047" target="_blank">동전 0</a>        | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |    ✅   |      
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21758" target="_blank">21758</a> | <a href="https://www.acmicpc.net/problem/21758" target="_blank">꿀 따기</a>       | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/>        |      
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16953" target="_blank">16953</a> | <a href="https://www.acmicpc.net/problem/16953" target="_blank">A → B</a>         | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |   ✅  |      
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


|번호|        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        문제 풀기         |  
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21608" target="_blank">21608</a> | <a href="https://www.acmicpc.net/problem/21608" target="_blank">상어 초등학교</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21611" target="_blank">21611</a> | <a href="https://www.acmicpc.net/problem/21611" target="_blank">마법사 상어와 블리자드</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/14.svg"/> |                      |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2753" target="_blank">2753</a> | <a href="https://www.acmicpc.net/problem/2753" target="_blank">윤년</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/2.svg"/> |✅ |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1212" target="_blank">1212</a> | <a href="https://www.acmicpc.net/problem/1212" target="_blank">8진수 2진수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/3.svg"/> |✅  |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20053" target="_blank">20053</a> | <a href="https://www.acmicpc.net/problem/20053" target="_blank">최소, 최대 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/3.svg"/> |✅  |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/5597" target="_blank">5597</a> | <a href="https://www.acmicpc.net/problem/5597" target="_blank">과제 안 내신 분..?</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> |✅ | 
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21918" target="_blank">21918</a> | <a href="https://www.acmicpc.net/problem/21918" target="_blank">전구</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> |✅  |
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20546" target="_blank">20546</a> | <a href="https://www.acmicpc.net/problem/20546" target="_blank">🐜 기적의 매매법 🐜</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/5.svg"/> |✅ |
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1913" target="_blank">1913</a> | <a href="https://www.acmicpc.net/problem/1913" target="_blank">달팽이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14467" target="_blank">14467</a> | <a href="https://www.acmicpc.net/problem/14467" target="_blank">소가 길을 건너간 이유 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |✅| 
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/12933" target="_blank">12933</a> | <a href="https://www.acmicpc.net/problem/12933" target="_blank">오리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | |
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2578" target="_blank">2578</a> | <a href="https://www.acmicpc.net/problem/2578" target="_blank">빙고</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | |
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/4396" target="_blank">4396</a> | <a href="https://www.acmicpc.net/problem/4396" target="_blank">지뢰 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/>| | 
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1244" target="_blank">1244</a> | <a href="https://www.acmicpc.net/problem/1244" target="_blank">스위치 켜고 끄기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> ||
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10994" target="_blank">10994</a> | <a href="https://www.acmicpc.net/problem/10994" target="_blank">별 찍기 - 19</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> ||
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20291" target="_blank">20291</a> | <a href="https://www.acmicpc.net/problem/20291" target="_blank">파일 정리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | |
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20436" target="_blank">20436</a> | <a href="https://www.acmicpc.net/problem/20436" target="_blank">ZOAC 3</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/7.svg"/> | |
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17413" target="_blank">17413</a> | <a href="https://www.acmicpc.net/problem/17413" target="_blank">단어 뒤집기 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> || 
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2615" target="_blank">2615</a> | <a href="https://www.acmicpc.net/problem/2615" target="_blank">오목</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                  |    
| 19 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16926" target="_blank">16926</a> | <a href="https://www.acmicpc.net/problem/16926" target="_blank">배열 돌리기 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | |
| 20 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15787" target="_blank">15787</a> | <a href="https://www.acmicpc.net/problem/15787" target="_blank">기차가 어둠을 헤치고 은하수를</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> ||                      
| 21 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17276" target="_blank">17276</a> | <a href="https://www.acmicpc.net/problem/17276" target="_blank">배열 돌리기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20207" target="_blank">20207</a> | <a href="https://www.acmicpc.net/problem/20207" target="_blank">달력</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | |
| 23 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/20164" target="_blank">20164</a> | <a href="https://www.acmicpc.net/problem/20164" target="_blank">홀수 홀릭 호석</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | |                     
| 24 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14719" target="_blank">14719</a> | <a href="https://www.acmicpc.net/problem/14719" target="_blank">빗물</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                |      
| 25 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16719" target="_blank">16719</a> | <a href="https://www.acmicpc.net/problem/16719" target="_blank">ZOAC</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |               |       


---
### DFS/BFS


|번호|        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        문제 풀기         |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2606" target="_blank">2606</a> | <a href="https://www.acmicpc.net/problem/2606" target="_blank">바이러스</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |  ✅   |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1260" target="_blank">1260</a> | <a href="https://www.acmicpc.net/problem/1260" target="_blank">DFS와 BFS</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |✅ |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11725" target="_blank">11725</a> | <a href="https://www.acmicpc.net/problem/11725" target="_blank">트리의 부모 찾기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | ✅ |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1325" target="_blank">1325</a> | <a href="https://www.acmicpc.net/problem/1325" target="_blank">효율적인 해킹</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | ✅ |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2178" target="_blank">2178</a> | <a href="https://www.acmicpc.net/problem/2178" target="_blank">미로 탐색</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |  | 
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2667" target="_blank">2667</a> | <a href="https://www.acmicpc.net/problem/2667" target="_blank">단지번호붙이기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/>   ||
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/7576" target="_blank">7576</a> | <a href="https://www.acmicpc.net/problem/7576" target="_blank">토마토</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | |
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/7569" target="_blank">7569</a> | <a href="https://www.acmicpc.net/problem/7569" target="_blank">토마토</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> ||
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16918" target="_blank">16918</a> | <a href="https://www.acmicpc.net/problem/16918" target="_blank">봄버맨</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> ||
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/5547" target="_blank">5547</a> | <a href="https://www.acmicpc.net/problem/5547" target="_blank">일루미네이션</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> ||
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14502" target="_blank">14502</a> | <a href="https://www.acmicpc.net/problem/14502" target="_blank">연구소</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> ||
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16234" target="_blank">16234</a> | <a href="https://www.acmicpc.net/problem/16234" target="_blank">인구 이동</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>  ||
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2636" target="_blank">2636</a> | <a href="https://www.acmicpc.net/problem/2636" target="_blank">치즈</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | |
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/13549" target="_blank">13549</a> | <a href="https://www.acmicpc.net/problem/13549" target="_blank">숨바꼭질 3</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/>  ||
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16954" target="_blank">16954</a> | <a href="https://www.acmicpc.net/problem/16954" target="_blank">움직이는 미로 탈출</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17836" target="_blank">17836</a> | <a href="https://www.acmicpc.net/problem/17836" target="_blank">공주님을 구해라!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16973" target="_blank">16973</a> | <a href="https://www.acmicpc.net/problem/16973" target="_blank">직사각형 탈출</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/14940" target="_blank">14940</a> | <a href="https://www.acmicpc.net/problem/14940" target="_blank">쉬운 최단거리</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/18513" target="_blank">18513</a> | <a href="https://www.acmicpc.net/problem/18513" target="_blank">샘터</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> | 
| 19 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2668" target="_blank">2668</a> | <a href="https://www.acmicpc.net/problem/2668" target="_blank">숫자고르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/13023" target="_blank">13023</a> | <a href="https://www.acmicpc.net/problem/13023" target="_blank">ABCDE</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/11.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1600" target="_blank">1600</a> | <a href="https://www.acmicpc.net/problem/1600" target="_blank">말이 되고픈 원숭이</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2206" target="_blank">2206</a> | <a href="https://www.acmicpc.net/problem/2206" target="_blank">벽 부수고 이동하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> | |
| 23 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2573" target="_blank">2573</a> | <a href="https://www.acmicpc.net/problem/2573" target="_blank">빙산</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 24 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/4179" target="_blank">4179</a> | <a href="https://www.acmicpc.net/problem/4179" target="_blank">불!</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 25 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/16932" target="_blank">16932</a> | <a href="https://www.acmicpc.net/problem/16932" target="_blank">모양 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 26 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1967" target="_blank">1967</a> | <a href="https://www.acmicpc.net/problem/1967" target="_blank">트리의 지름</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/12.svg"/> |                      |
| 27 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9466" target="_blank">9466</a> | <a href="https://www.acmicpc.net/problem/9466" target="_blank">텀 프로젝트</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/13.svg"/> |                      |


---
### 정렬



---
### 이진탐색



---
### 동적계획법1


|번호|        추천 문제         |        문제 번호         |        문제 이름         |         난이도          |        문제 풀기         |    한줄평 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| 00 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10870" target="_blank">10870</a> | <a href="https://www.acmicpc.net/problem/10870" target="_blank">피보나치 수 5</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/4.svg"/> |✅ |
| 01 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2839" target="_blank">2839</a> | <a href="https://www.acmicpc.net/problem/2839" target="_blank">설탕 배달</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/5.svg"/> |✅ |
| 02 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2748" target="_blank">2748</a> | <a href="https://www.acmicpc.net/problem/2748" target="_blank">피보나치 수 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/5.svg"/> |✅ |
| 03 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1010" target="_blank">1010</a> | <a href="https://www.acmicpc.net/problem/1010" target="_blank">다리 놓기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | |
| 04 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9655" target="_blank">9655</a> | <a href="https://www.acmicpc.net/problem/9655" target="_blank">돌 게임</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> |                      |
| 05 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/17626" target="_blank">17626</a> | <a href="https://www.acmicpc.net/problem/17626" target="_blank">Four Squares</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/6.svg"/> | |
| 06 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1463" target="_blank">1463</a> | <a href="https://www.acmicpc.net/problem/1463" target="_blank">1로 만들기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | |
| 07 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9095" target="_blank">9095</a> | <a href="https://www.acmicpc.net/problem/9095" target="_blank">1, 2, 3 더하기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | |
| 08 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11726" target="_blank">11726</a> | <a href="https://www.acmicpc.net/problem/11726" target="_blank">2×n 타일링</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | |
| 09 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2579" target="_blank">2579</a> | <a href="https://www.acmicpc.net/problem/2579" target="_blank">계단 오르기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 10 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11727" target="_blank">11727</a> | <a href="https://www.acmicpc.net/problem/11727" target="_blank">2×n 타일링 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> | |
| 11 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/22857" target="_blank">22857</a> | <a href="https://www.acmicpc.net/problem/22857" target="_blank">가장 긴 짝수 연속한 부분 수열 (small)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/8.svg"/> |                      |
| 12 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11053" target="_blank">11053</a> | <a href="https://www.acmicpc.net/problem/11053" target="_blank">가장 긴 증가하는 부분 수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | |
| 13 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1912" target="_blank">1912</a> | <a href="https://www.acmicpc.net/problem/1912" target="_blank">연속합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 14 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/9465" target="_blank">9465</a> | <a href="https://www.acmicpc.net/problem/9465" target="_blank">스티커</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 15 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11055" target="_blank">11055</a> | <a href="https://www.acmicpc.net/problem/11055" target="_blank">가장 큰 증가 부분 수열</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> | |
| 16 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1890" target="_blank">1890</a> | <a href="https://www.acmicpc.net/problem/1890" target="_blank">점프</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 17 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2407" target="_blank">2407</a> | <a href="https://www.acmicpc.net/problem/2407" target="_blank">조합</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 18 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/1106" target="_blank">1106</a> | <a href="https://www.acmicpc.net/problem/1106" target="_blank">호텔</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/9.svg"/> |                      |
| 19 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/15486" target="_blank">15486</a> | <a href="https://www.acmicpc.net/problem/15486" target="_blank">퇴사 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 20 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2156" target="_blank">2156</a> | <a href="https://www.acmicpc.net/problem/2156" target="_blank">포도주 시식</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 21 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/10844" target="_blank">10844</a> | <a href="https://www.acmicpc.net/problem/10844" target="_blank">쉬운 계단 수</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 22 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2293" target="_blank">2293</a> | <a href="https://www.acmicpc.net/problem/2293" target="_blank">동전 1</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 23 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/2294" target="_blank">2294</a> | <a href="https://www.acmicpc.net/problem/2294" target="_blank">동전 2</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |
| 24 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/11660" target="_blank">11660</a> | <a href="https://www.acmicpc.net/problem/11660" target="_blank">구간 합 구하기 5</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | |
| 25 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/21317" target="_blank">21317</a> | <a href="https://www.acmicpc.net/problem/21317" target="_blank">징검다리 건너기</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> | |
| 26 |  :heavy_check_mark:  | <a href="https://www.acmicpc.net/problem/22869" target="_blank">22869</a> | <a href="https://www.acmicpc.net/problem/22869" target="_blank">징검다리 건너기 (small)</a> | <img height="25px" width="25px" src="https://static.solved.ac/tier_small/10.svg"/> |                      |


---
### 동적계획법2



---
### 최단 경로



---
### 그래프 탐색


