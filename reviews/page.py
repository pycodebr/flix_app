import pandas as pd
import streamlit as st
from reviews.service import ReviewService
from st_aggrid import AgGrid, ExcelExportMode


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        st.write('Lista de Avaliações:')
        reviews_df = pd.json_normalize(reviews)
        AgGrid(
            data=reviews_df,
            reload_data=True,
            columns_auto_size_mode=True,
            enableSorting=True,
            enableFilter=True,
            enableColResize=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')
