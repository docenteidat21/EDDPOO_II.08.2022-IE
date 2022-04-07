class DocumentoVenta:

    def __init__(self, nDocumentoVenta, fecha, igv, totalPrecioVenta):

        self.nDocumentoVenta = nDocumentoVenta
        self.fecha = fecha
        self.igv = igv
        self.totalPrecioVenta = totalPrecioVenta
        self.estado = "Vigente" 
