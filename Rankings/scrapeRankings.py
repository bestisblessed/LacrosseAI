from bs4 import BeautifulSoup

def extract_and_save_rankings_with_headers(input_html_file, output_txt_file):
    # Load the HTML content from the provided file
    with open(input_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all table rows in the document
    table_rows = soup.find_all('tr')

    # Open the output file to write the rankings
    with open(output_txt_file, 'w', encoding='utf-8') as file:
        # First, extract and write the headers
        header_row = ' '.join(table_rows[0].stripped_strings)
        file.write(f"{header_row}\n")

        # Then, skip the header rows and extract the rankings from the rest
        for row in table_rows[2:]:  # Adjust the index if the header size changes
            # Combine the strings from each row, stripping any leading/trailing whitespace
            row_text = ' '.join(row.stripped_strings)
            file.write(f"{row_text}\n")

    print(f"Rankings along with headers have been extracted to {output_txt_file}")

# Specify the path to your HTML file and the desired output text file
input_html_file = './data/rankings.html'
output_txt_file = './data/rankings.txt'

# Call the function with the paths
extract_and_save_rankings_with_headers(input_html_file, output_txt_file)

