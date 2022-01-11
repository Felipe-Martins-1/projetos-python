from flask import flash


class WallPaintQuantity:
    def __init__(self) -> None:

        # Variável armazena o valor total da área disponível
        self.total_area = 0.0

        # Dicionário que armazena outras variáveis
        self.tins = {}

    # Função que valida os valores de acordo com as regras de negócio
    # Retorna um valor lógico: True ou False
    def __validate_values(self, values: dict) -> bool:

        # Variáveis constantes
        PORT_HEIGHT = 1.9
        PORT_WIDTH = 0.8
        WIND_HEIGHT = 1.2
        WIND_WIDTH = 2

        # Variável de controle
        status = True

        # Faz o cálculo de cada parede
        for i in range(1, 5):
            # print(f"\nParede = {i}")

            # Área da parede
            area_hei_wid = float(values[f"height_{i}"]) * float(values[f"width_{i}"])
            # print(f"ÁREA PAREDE = {area_hei_wid}")

            # Valida a área da parede, a mesma tem que valer maior ou igual a 1 e menor
            # ou igual a 15
            if area_hei_wid >= 1 and area_hei_wid <= 15:

                # Área da porta
                port_area = PORT_HEIGHT * PORT_WIDTH * int(values[f"por_quant_{i}"])
                # print(f"ÁREA PORTA = {port_area}")

                # Área da janela
                wind_area = WIND_HEIGHT * WIND_WIDTH * int(values[f"win_quant_{i}"])
                # print(f"ÁREA JANELA = {wind_area}")

                # Soma da área da porta e janela
                area_port_wind = port_area + wind_area
                # print(f"ÁREA PORTA + JANELA = {area_port_wind}")

                # Porcentagem da soma da área da porta e janela em relação a área da parede
                area_perc = (area_port_wind * 100) / area_hei_wid
                # print(f"PORCENTAGEM ÁREA JANELA + PORTA = {area_perc}%")

                # Valida a porcentagem da soma da área da porta e janela, a porcentagem tem
                # que ser menor ou igual a 50%
                if area_perc <= 50:

                    # Diferença de altura da parede em relação a porta
                    port_wall_diff = float(values[f"height_{i}"]) - PORT_HEIGHT
                    # print(f"DIFERENÇA ALTURA PAREDE - PORTA  = {port_wall_diff}")

                    # Valida a diferença de altura da parede em relação a porta, tem que valer
                    # mais ou igual a 30cm
                    if port_wall_diff >= 0.3:
                        # print(f"DIFERENÇA ÁREA HEI_WID - PORT_WIND = {area_hei_wid - area_port_wind}")

                        # Soma total da área disponível para pintar
                        self.total_area = self.total_area + (
                            area_hei_wid - area_port_wind
                        )
                        flash("")
                    else:
                        flash(
                            f"Parede {i}: a diferença da altura da parede e da porta é menor que 30cm"
                        )
                        # print(f"Parede {i}: a diferença da altura da parede e da porta é menor que 30cm")
                        status = False
                        break
                else:
                    flash(
                        f"Parede {i}: a soma da área da janela e da porta corresponde a mais de 50% da área da parede"
                    )
                    # print(f"Parede {i}: a soma da área da janela e da porta corresponde a mais de 50% da área da parede")
                    status = False
                    break
            else:
                flash(f"Parede {i}: o metro quadrado da parede não é aceito")
                # print(f"Parede {i}: o metro quadrado da parede não é aceito")
                status = False
                break
        return status

    # Função que calcula a quantidade de tinta e de latas necessárias
    # Não tem retorno
    def calculate_quantity(self, values: dict) -> None:

        # A cada solicitação o dicionário inteiro é apagado
        self.tins.clear()

        # Retorno True
        if self.__validate_values(values):

            # Variáveis que correspondem as latas de tinta
            tin_18 = 0
            tin_3 = 0
            tin_2 = 0
            tin_05 = 0

            # print(f"\nÁREA TOTAL PINTAR = {self.total_area}")

            # Litros necessários
            liters_needed = self.total_area / 5
            # print(f"LITROS NECESSÁRIOS = {liters_needed}")

            # Litros necessários em valor inteiro
            liters_int = self.total_area // 5
            # print(f"LITROS INTEIRO = {liters_int}")

            # Diferença dos litros necessários em relação aos litros de valor inteiro
            diff_liters = liters_needed - liters_int
            # print(f"DIFERENÇA DE LITROS = {diff_liters}")

            # Dependendo da diferença entre os litros é acrescentado ou não um valor
            # nos litros
            if diff_liters > 0 and diff_liters < 0.5:
                liters = ((0.5 - diff_liters) + diff_liters) + liters_int
            elif diff_liters > 0.5 and diff_liters < 1:
                liters = ((1 - diff_liters) + diff_liters) + liters_int
            else:
                liters = liters_needed

            # print(f"LITROS = {liters}")

            # Quantidade de cada lata
            while liters >= 18:
                tin_18 += 1
                liters -= 18
            while liters >= 3.6:
                tin_3 += 1
                liters -= 3.6
            while liters >= 2.5:
                tin_2 += 1
                liters -= 2.5
            while liters >= 0.5:
                tin_05 += 1
                liters -= 0.5

            # As variáveis que tem valor setado são acrescentadas ao dicionário
            if tin_18:
                self.tins["18"] = tin_18
            if tin_3:
                self.tins["3,6"] = tin_3
            if tin_2:
                self.tins["2,5"] = tin_2
            if tin_05:
                self.tins["0,5"] = tin_05

            """print(f"\n18 LITROS = {tin_18}")
            print(f"3,6 LITROS = {tin_3}")
            print(f"2,5 LITROS = {tin_2}")
            print(f"0,5 LITROS = {tin_05}")"""

            # A cada solicitação recebe o valor 0
            self.total_area = 0
