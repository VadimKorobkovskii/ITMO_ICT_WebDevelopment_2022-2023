**Таблица для хранения данных о зарегистрированных экспертах.**
 
`Таблица имеет следующие поля:`
:

  1. Поле "show_exp_number" хранит порядковый номер эксперта на выставке

  2. Поле "exp_status" хранит статус эксперта, который надо выбрать из списка

  3. Поле "reg_exp_date" хранит дату регистрации эксперта

  4. Поле "participant_exp" является внешним ключом к таблице Expert

  5. Поле "show_exp" является внешним ключом к таблице Show

## Списки для выбора:

### Cписок для поля "exp_status"

``` python
status_choices = (
        ("Участвовал/Participated", "Участвовал/Participated"),
        ("Снят/Suspended", "Снят/Suspended"),
        ("Не допущен/Not allowed", "Не допущен/Not allowed"),
        ("Неявка/Absence", "Неявка/Absence")
)
```
