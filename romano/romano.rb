class Romano
  def initialize numero
    @numero = numero
  end

  def to_roman
    case @numero
      when 1
	"I"
      when 2
        "II"
      when 3
	"III"
      when 4
        "IV"
    end    
  end
end
