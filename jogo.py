def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] != " ":
            return tabuleiro[0][col]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]
    return None

def jogo_da_velha():
    tabuleiro = [[" "]*3 for _ in range(3)]
    jogador = "X"
    for turno in range(9):
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador}")
        linha = int(input("Linha (0, 1, 2): "))
        coluna = int(input("Coluna (0, 1, 2): "))
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor:
                exibir_tabuleiro(tabuleiro)
                print(f"🎉 Jogador {vencedor} venceu!")
                return
            jogador = "O" if jogador == "X" else "X"
        else:
            print("Posição ocupada. Tente novamente.")
    exibir_tabuleiro(tabuleiro)
    print("Empate!")

if __name__ == "__main__":
    jogo_da_velha()
