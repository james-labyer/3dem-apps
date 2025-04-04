FROM eriksf/fiji:openjdk-8-ui

RUN ln -s /tmp/ImageJ.cfg /opt/fiji/Fiji.app/ImageJ.cfg

COPY run.sh /tapis/run.sh

RUN chmod +x /tapis/run.sh

ENTRYPOINT [ "/tapis/run.sh" ]

CMD ["1280x800"]