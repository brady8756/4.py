#包含 < iostream >
#包含 < iomanip >
#包含“ OX.h ”
使用 命名空間 std ；



int 主（）{
    srand (時間( NULL )); //隨機定義通知
    OX遊戲；
    INT 選擇= 0 ; //選擇
    int位置 = 0 ,回合= 1 ; //畫的位置，截圖
    bool完成 = false , comFirst = true ; //遊戲是否結束，人機大戰時電腦是否先手

    COUT << “請選擇遊戲模式：” << ENDL << “ 1.人機大戰2.人人大戰（按0退出）： ” ;
    cin >>選擇;
    開關（選擇）{
    case  0 : //退出
        打破;
    case  1 : //人機大戰
        //決定先後手
        comFirst = 遊戲。誰第一（）;

        if ( select == 0 ) //玩家選擇退出
            打破;
        //遊戲開始
        遊戲。畫(); //畫格子
        cout << "格子對照數字鍵盤(按0退出) " << endl;

        while (!finish) { //遊戲是否結束
            if (comFirst) { //判斷主觀
                位置 =蘭特() % 9 + 1 ; // 1`9個隨機跑數字
                if ( game.setPosition (position, round )) { //如果可放，輸入回傳true，把電腦的出手調回後出手
                    comFirst =假；
                }
            }
            else { //玩家的同意
                cin >> 位置；
                if ( game.setPosition (position, round )) { //如果可放，輸入回傳true，把電腦的出手調回先出手
                    comFirst =真;
                }
                其他{
                    遊戲。錯(); //玩家按錯才輸出錯誤訊息，電腦按錯還跳錯誤訊息太丟臉
                }
            }
            if (position == 0 ) { //玩家決定退出遊戲
                完成 =真; //直接遊戲結束
                打破;
            }

            系統（“ CLS ”）；//清理畫面
            遊戲。畫();
            cout << "格子對照數字鍵盤(按0退出) " << endl;

            完成 = 遊戲。遊戲結束（）；//判斷是否有人贏了
            如果（完成）{
                回合% 2 == 1 ? cout<< “ X ”：cout<< “ O ”；//通過選擇數字決定這是誰出手
                cout << "贏了" << endl;
            }
            else  if ( round > 9 ) { //超過9次仍無人贏
                打破; //跳出迴圈
            }
        }
        如果（！完成）
            cout << "平手" << endl;

        打破;

    案例 2：//人
        遊戲。畫();
        cout << "格子對照數字鍵盤(按0退出) " << endl;
        而（！完成）{
            cin >> 位置；
            如果（位置== 0）{
                完成 =真;
                打破;
            }
            if (! game.setPosition (position, round ))
                遊戲。錯();
            系統（“ CLS ”）；
            遊戲。畫();
            cout << "格子對照數字鍵盤(按0退出) " << endl;
            完成 = 遊戲。遊戲結束（）；
            如果（完成）{
                回合% 2 == 1 ? cout<< “ X ”：cout<< “ O ”；
                cout << "贏了" << endl;
            } else  if ( round > 9 ) { //超過9次仍無人贏
                打破; //跳出迴圈
            }
        }
        如果（！完成）
            cout << "平手" << endl;
        打破;
    }

    返回 0 ;
}
