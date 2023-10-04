Для проектирования классов очень часто используется язык UML (Unified Modeling Language)


Онлайн можно посмотреть в plantuml.com


https://plantuml.com/ru/class-diagram
Пример:

@startuml
class Customer{
  + name
  + address

  send_order()
  receive_order()
}

class Order{
  + date
  + number

  confirm()
  close()
}

class SpecialOrder{

  + date
  + number

  #private_client

  confirm()
  close()
  dispatch()
}

class NormalOrder{

  + date
  + number

  confirm()
  close()
  dispatch()
  receive()
}

Customer "1" -- "n" Order
Order <|-- SpecialOrder
Order <|-- NormalOrder


@enduml


www.plantuml.com/plantuml/png/XT0xJiOm30VmtQUmmW927TWPAh73m06g41iHAO_AJhe0ToVqyIbBrIMA_r9-ZZrgiL9g3E22LSMNgYL7bcz0VCHa8wyNIoIi2grGJZHb8PRxXrOAE_OBtv9VsAKteOCXMtZpQlnW-LTSJfzUuagua9Nxf-ypEs_3BfmHTxFufSMJ2vvJELCHoUjiY_lgMxncYHSThhX-_8q-beVcoU0me4bcMmEi9px_jB0Vhilx7m70o8bg37y0