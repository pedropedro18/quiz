import json
import os
from datetime import datetime

FICHEIRO = "pontuacoes.json"

PERGUNTAS = [
    {"pergunta": "Qual é a capital de Portugal?",
     "opcoes": ["Porto", "Lisboa", "Coimbra", "Faro"], "resposta": 2},
    {"pergunta": "Quantos continentes existem?",
     "opcoes": ["5", "6", "7", "8"], "resposta": 3},
    {"pergunta": "Quem escreveu 'Os Lusíadas'?",
     "opcoes": ["Fernando Pessoa", "Camões", "Eça de Queirós", "Saramago"], "resposta": 2},
    {"pergunta": "Qual é o maior oceano?",
     "opcoes": ["Atlântico", "Índico", "Pacífico", "Ártico"], "resposta": 3},
    {"pergunta": "Quanto é 12 x 12?",
     "opcoes": ["124", "144", "148", "164"], "resposta": 2},
]


def carregar():
    if os.path.exists(FICHEIRO):
        try:
            with open(FICHEIRO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def guardar(registos):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(registos, f, ensure_ascii=False, indent=2)


def perguntar(p):
    print(f"\n{p['pergunta']}")
    for i, op in enumerate(p["opcoes"], 1):
        print(f"  {i}) {op}")
    while True:
        r = input("Resposta (1-4): ").strip()
        if r in ("1", "2", "3", "4"):
            return int(r) == p["resposta"]
        print("Opção inválida.")


def main():
    nome = input("O teu nome: ").strip() or "Anónimo"
    pontos = sum(perguntar(p) for p in PERGUNTAS)
    total = len(PERGUNTAS)
    print(f"\n{nome}, acertaste {pontos}/{total}!")

    registos = carregar()
    registos.append({
        "nome": nome,
        "pontos": pontos,
        "total": total,
        "data": datetime.now().isoformat(timespec="seconds"),
    })
    guardar(registos)

    print("\n🏆 Melhores pontuações:")
    melhores = sorted(registos, key=lambda r: r["pontos"], reverse=True)[:5]
    for i, r in enumerate(melhores, 1):
        print(f"  {i}. {r['nome']} - {r['pontos']}/{r['total']} ({r['data'][:10]})")


if __name__ == "__main__":
    main()
