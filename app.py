import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="GC麻雀 記録管理アプリ", page_icon="🀄", layout="wide"
)

st.title("🀄 GC麻雀 成績管理ダッシュボード")

# タブの作成
tab1, tab2 = st.tabs(["📊 各種記録・閲覧", "✍️ 成績インプット"])

# --- タブ1: 閲覧画面 ---
with tab1:
  st.subheader("🏆 プレイヤー各種記録・ランキング")
  try:
    df_rec = pd.read_csv("GC麻雀記録ファイル_各種記録.csv")
    st.dataframe(df_rec, use_container_width=True)
  except FileNotFoundError:
    st.warning("各種記録のデータが見つかりません。")

  st.subheader("📈 成績インプット履歴（直近データ）")
  try:
    df_input = pd.read_csv("GC麻雀記録ファイル_成績インプット.csv")
    st.dataframe(df_input, use_container_width=True)
  except FileNotFoundError:
    st.warning("成績インプットのデータが見つかりません。")

# --- タブ2: インプット画面 ---
with tab2:
  st.subheader("📝 新規ゲーム成績の登録 (プレビュー)")
  st.info(
      "※現在は閲覧モードです。ここにインプットフォームを拡張して、みんなで"
      "Googleスプレッドシート等へ書き込めるように連携できます！"
  )

  with st.form("input_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
      game_date = st.date_input("対戦日時")
    with col2:
      game_type = st.selectbox("ゲーム形式", ["東風戦", "半荘戦", "三麻"])
    with col3:
      rate = st.number_input("レート", value=30.0)

    st.markdown("### 各プレイヤーのスコア入力")
    col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
    with col_p1:
      score_hirano = st.number_input("平野", value=0.0)
    with col_p2:
      score_take = st.number_input("武範", value=0.0)
    with col_p3:
      score_kyo = st.number_input("恭平", value=0.0)
    with col_p4:
      score_ami = st.number_input("亜美", value=0.0)
    with col_p5:
      score_yuta = st.number_input("雄太", value=0.0)

    submitted = st.form_submit_button("成績を追加する")
    if submitted:
      st.success("（デモ）成績データを受け付けました！")
