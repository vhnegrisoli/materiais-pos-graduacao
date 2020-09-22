import lombok.SneakyThrows;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.util.StringTokenizer;

public class Map extends Mapper<LongWritable, Text, Text, IntWritable> {

    private static final IntWritable UM = new IntWritable(1);
    private Text palavra = new Text();

    @SneakyThrows
    public void map(LongWritable key, Text value, Context context) {
        var linha = value.toString();
        var tokenizer = new StringTokenizer(linha);
        while (tokenizer.hasMoreTokens()) {
            palavra.set(tokenizer.nextToken());
            context.write(palavra, UM);
        }
    }
}
