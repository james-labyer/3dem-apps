FROM jlabyer/napari:0.0.7

COPY --from=taccaci/interactive-base:1.1.0 /tapis /tapis

ENTRYPOINT [ "/tapis/run.sh"]
