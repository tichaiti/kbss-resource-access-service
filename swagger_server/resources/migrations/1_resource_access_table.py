
from yoyo import step

# -----------------------------------------------------------------------------------------------------------------
# -- Tables
# -----------------------------------------------------------------------------------------------------------------

step("""
CREATE TABLE resource_access  (
    id              serial PRIMARY KEY,
    user_id         text,
    resource_id     text,
    resource_type   text
)
""")
