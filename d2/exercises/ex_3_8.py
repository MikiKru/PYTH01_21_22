months = ('styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień')

quarters = [[month for m_index, month in enumerate(months) if m_index // 3 == q_index] for q_index in range(4)]
# for q_index in range(4):
#     current_months = []
#     for m_index, month in enumerate(months):
#         if m_index // 3 == q_index:
#             current_months.append(month)
#     quarters.append(current_months)

print(quarters)