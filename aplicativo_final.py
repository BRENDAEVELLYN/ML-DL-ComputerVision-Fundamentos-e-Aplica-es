# importação do opencv-python
import cv2


# criar uma variável para camera
cap = cv2.VideoCapture(0)

# enquanto a camera estiver aberta
while cap.isOpened():
    #sucesso - booleana (verificar se o frame esta vazio)
    #frame - captura
    sucesso, frame = cap.read()
    # realizar a verificação
    # sucesso = 1 fracasso = 0
    if not sucesso:
        print("ignorando o frame vazio da câmera")
        continue
    #carregar nosso frame - com titulo
    cv2.imshow('Camera', frame)
    # bitwise - tabela ASC II
    # 10 milissegundos
    # ord() - retorna o valor unicode ou ASC II
    # o valor 0xFF é da tabela  ASC II ESTENDIDA
    if cv2.waitKey(10) & 0xFF ==ord('c'):
        break   
cap.release()
cv2.destroyAllWindows()
