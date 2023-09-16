add_library (pyhanabi SHARED pyhanabi.cc)
target_link_libraries (pyhanabi LINK_PUBLIC hanabi)

install(TARGETS pyhanabi LIBRARY DESTINATION hana_learn)
install(FILES __init__.py DESTINATION hana_learn)
install(FILES rl_env.py DESTINATION hana_learn)
install(FILES pyhanabi.py DESTINATION hana_learn)
install(FILES pyhanabi.h DESTINATION hana_learn)
