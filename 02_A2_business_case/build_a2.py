import openpyxl
from openpyxl.chart import BarChart, Reference
from openpyxl.utils import get_column_letter

def build_a2_workbook():
    src_path = "02_A2_business_case/A2_GenAI_Cost_ROI_reference.xlsx"
    dst_path = "02_A2_business_case/A2_GenAI_Cost_ROI.xlsx"

    wb_src = openpyxl.load_workbook(src_path, data_only=False)
    wb_dst = openpyxl.Workbook()
    # remove default sheet
    wb_dst.remove(wb_dst.active)

    # Copy sheets
    for sheet_name in wb_src.sheetnames:
        ws_src = wb_src[sheet_name]
        ws_dst = wb_dst.create_sheet(title=sheet_name)
        
        # Copy column dimensions
        for col_letter, col_dim in ws_src.column_dimensions.items():
            ws_dst.column_dimensions[col_letter].width = col_dim.width
            
        # Copy row dimensions
        for r_idx, row_dim in ws_src.row_dimensions.items():
            ws_dst.row_dimensions[r_idx].height = row_dim.height

        # Copy cells with values, formulas, and formatting
        for row in ws_src.iter_rows():
            for cell in row:
                new_cell = ws_dst.cell(row=cell.row, column=cell.column, value=cell.value)
                if cell.has_style:
                    new_cell.font = openpyxl.styles.Font(
                        name=cell.font.name, size=cell.font.size, bold=cell.font.bold,
                        italic=cell.font.italic, color=cell.font.color
                    )
                    new_cell.alignment = openpyxl.styles.Alignment(
                        horizontal=cell.alignment.horizontal, vertical=cell.alignment.vertical,
                        wrap_text=cell.alignment.wrap_text
                    )
                    new_cell.number_format = cell.number_format
                    if cell.fill and cell.fill.fill_type:
                        new_cell.fill = openpyxl.styles.PatternFill(
                            fill_type=cell.fill.fill_type,
                            start_color=cell.fill.start_color,
                            end_color=cell.fill.end_color
                        )
                    if cell.border:
                        new_cell.border = openpyxl.styles.Border(
                            left=cell.border.left, right=cell.border.right,
                            top=cell.border.top, bottom=cell.border.bottom
                        )

    # Copy defined names
    for name, defn in wb_src.defined_names.items():
        wb_dst.defined_names.add(defn)

    # Re-attach Tornado Chart on Tornado sheet
    ws_tor = wb_dst["Tornado"]
    chart = BarChart()
    chart.type = "bar"
    chart.style = 10
    chart.title = "Change in NPV vs base (₹ lakh)"
    chart.y_axis.title = "Driver"
    chart.x_axis.title = "₹ lakh swing"
    chart.height = 10
    chart.width = 16

    data = Reference(ws_tor, min_col=4, min_row=1, max_col=5, max_row=9)
    cats = Reference(ws_tor, min_col=1, min_row=2, max_row=9)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    ws_tor.add_chart(chart, "B12")

    wb_dst.save(dst_path)
    print(f"Successfully generated custom workbook: {dst_path}")

if __name__ == "__main__":
    build_a2_workbook()
