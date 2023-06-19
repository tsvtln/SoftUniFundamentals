from math import floor as flr


def factory(biscuit_pd: int, workers: int, comp_factory_production: int):
    MORE = False
    produced_biscuits = 10 * (flr((entry_biscuits_pd * workers) * 0.75)) + (20 * (entry_biscuits_pd * workers))
    if produced_biscuits > comp_factory_production:
        difference = produced_biscuits - comp_factory_production
        pct = (difference / comp_factory_production) * 100
        MORE = True
    else:
        difference = comp_factory_production - produced_biscuits
        pct = (difference / comp_factory_production) * 100
        MORE = False
    return produced_biscuits, pct, MORE


entry_biscuits_pd, entry_workers, entry_competing_factory = int(input()), int(input()), int(input())
pb, pctr, MORER = factory(entry_biscuits_pd, entry_workers, entry_competing_factory)

print(f"You have produced {pb} biscuits for the past month.\nYou produce {pctr:.2f} percent more biscuits.") if MORER \
    else print(f"You have produced {pb} biscuits for the past month.\nYou produce {pctr:.2f} percent less biscuits.")
