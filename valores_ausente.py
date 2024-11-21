import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar dados e verificar valores ausentes
def load_and_check_data(file_path):
    # Carregar o DataFrame
    df = pd.read_csv(file_path, delimiter=';')
    
    # Exibir as primeiras linhas do DataFrame
    print("Primeiras linhas do DataFrame:")
    print(df.head())
    
    # Verificar valores ausentes
    missing_values = df.isnull().sum()
    
    # Exibir valores ausentes
    print("\nValores ausentes por coluna:")
    print(missing_values[missing_values > 0])
    
    return df, missing_values

# Função para visualizar a proporção de valores ausentes
def plot_missing_values(missing_values):
    plt.figure(figsize=(10, 5))
    missing_percentage = (missing_values / len(df)) * 100
    missing_percentage.plot(kind='bar', color='skyblue')
    plt.title('Proporção de Valores Ausentes por Coluna')
    plt.xlabel('Colunas')
    plt.ylabel('Porcentagem de Valores Ausentes')
    plt.xticks(rotation=45)
    plt.axhline(0, color='grey', linewidth=0.8)
    plt.show()

# Caminho para o arquivo CSV
file_path = 'C:\\Users\\nickl\\OneDrive\Desktop\\varredo_de_valores_ausente\\dataset.csv'

# Executar as funções
df, missing_values = load_and_check_data(file_path)
plot_missing_values(missing_values)