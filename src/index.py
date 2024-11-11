from varasto import Varasto


def main():
    mehua, olutta = Varasto(100.0), Varasto(100.0, 20.2)

    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}\n"
          f"Olut getterit:\nsaldo = {olutta.saldo}\n"
          f"tilavuus = {olutta.tilavuus}\n"
          f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}\n"
          f"Mehu setterit:\nLisätään 50.7")

    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}\nVirhetilanteita:\nVarasto(-100.0);\n"
          f"{Varasto(-100.0)}\n"
          f"Varasto(100.0, -50.7)\n{Varasto(100.0, -50.7)}\n"
          f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\nMehuvarasto: {mehua}\n"
          f"mehua.lisaa_varastoon(-666.0)")

    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\nOlutvarasto: {olutta}\n"
          f"olutta.ota_varastosta(1000.0)")

    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\nOlutvarasto: {olutta}\n"
          f"Mehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)")

    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\nMehuvarasto: {mehua}")

    print("rikotaan pylint sääntö")

if __name__ == "__main__":
    main()
