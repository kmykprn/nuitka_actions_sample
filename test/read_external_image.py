# 外部ディレクトリ画像を表示できるかを確認するコード
import cv2

image = cv2.imread("image/daruma.jpg")

if image is None:
    print("画像を読み込めませんでした。ファイルパスを確認してください。")
else:
    # 表示したいサイズを指定（幅と高さ）
    new_width = 400  # 好みの幅（例: 400px）
    new_height = 550  # 好みの高さ（例: 700px）

    # リサイズ
    resized_image = cv2.resize(image, (new_width, new_height))

    # 画像をウィンドウに表示
    cv2.imshow("Resized Image", resized_image)

    # キー入力を待つ（0なら無限に待機）
    cv2.waitKey(0)

    cv2.destroyAllWindows()