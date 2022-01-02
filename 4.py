import  React ,  {  Component  }  from  'react' ;
 從'./Game.module.scss'導入樣式 ； 

const  toSymbol  =  ( n )  =>  {
    開關 ( n )  {
        案例 0：
            返回 '' ;
        案例 1：
            返回 'O' ;
        案例 - 1：
        默認：
            返回 “X” ；
    }
}

const 行 =  [
    [ 0 ,  1 ,  2 ] ,
    [ 3 ,  4 ,  5 ] ,
    [ 6 ,  7 ,  8 ] ,
    [ 0 ,  3 ,  6 ] ,
    [ 1 ,  4 ,  7 ] ,
    [ 2 ,  5 ,  8 ] ,
    [ 0 ,  4 ,  8 ] ,
    [ 2 ,  4 ,  6 ] ,
]

類 游戲 擴展 組件 {
    狀態 =  {
        網格：[ 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ] ,
        玩家: 1 ,
        獲勝者：0 ，
    }

    componentDidUpdate ( prevProps ,  PrevState )  {
        如果 （PrevState 。網格 ！== 這個。狀態。電網） {
            這個。設置狀態（{
                獲勝者：這個。獲得贏家( ) ,
            } )
        }
    }

    getWinner  =  ( )  =>  {
        const  {網格}  =  this 。狀態；
        for  ( const  line  of  lines )  {
            const  [ i ,  j ,  k ]  =  line ;
            if  (網格[ i ]  === 網格[ j ]  && 網格[ j ]  === 網格[ k ]  && 網格[ i ]  !==  0 )  {
                返回 網格[ i ] ;
            }
        }
        返回 0 ;
    }

    handleClick  =  ( idx )  =>  ( )  =>  {
        如果 （這個。狀態。贏家 ！==  0 ） 返回；
        const 網格 =  [ ...這個。狀態。網格] ;
        如果 （網格[ idx ]  ！==  0 ） 返回；

        網格[ idx ]  = 這個。狀態。播放器；
        這個。設置狀態（{
            網格，
            玩家：-這個。狀態。玩家，
        } )
    }

    重置 =  ( )  =>  {
        這個。設置狀態（{
            網格：[ 0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ] ,
            玩家: 1 ,
        } )
    } ;

    渲染( )  {
        const  {網格，玩家，獲勝者}  =  this 。狀態；
        返回 (
            < div  className = {樣式。遊戲} >
                < div  className = {樣式。板} >
                    {
                        網格。地圖( ( n ,  idx )  =>  (
                            < div
                                鍵= { `grid- ${ idx } ` }
                                類名= {樣式。網格}
                                onClick = {這個。處理點擊（idx ）}
                            >
                                < span > { toSymbol ( n ) } < / span >
                            < / div >
                        ) )
                    }
                < / div >
                < div  className = {樣式。信息} >
                    < div  className = {樣式。標題} > < u > TIC TAC TOE < / u > < / div >
                    播放器：{ toSymbol (播放器) } < br  / >
                    WINNER：{ toSymbol (獲勝者) } < br  / >
                    <按鈕
                        類名= {樣式。親愛的}
                        onClick = {這個。重置}
                    >
                        重啟                                                              
                    < /按鈕>
                < / div >
            < / div >
        ) ;
    }
}

導出 默認 遊戲；
